import yaml
import pprint
from yaml.events import ScalarEvent, MappingStartEvent

def ankorpin_process_and_remap(input_path, output_path):
  with open(input_path, 'r', encoding='utf-8') as f:
    yaml_text = f.read()

  events = list(yaml.parse(yaml_text))
  modified_events = []

  current_section = None
  pending_index = None
  
  prefixes = {
    'tnorms': 'tnorm',
    'tpolls': 'tpoll',
    'sigs': 'sig',
    'glbda': 'gda'
  }

  for event in events:
    if isinstance(event, ScalarEvent):
      if event.value in prefixes:
        current_section = event.value
      elif current_section and event.value.isdigit():
        pending_index = event.value

    elif isinstance(event, MappingStartEvent) and pending_index:
      prefix = prefixes[current_section]
      anchor_name = f"{prefix}{pending_index}-ank"
      
      event = MappingStartEvent(
        anchor=anchor_name,
        tag=event.tag,
        implicit=event.implicit,
        start_mark=event.start_mark,
        end_mark=event.end_mark,
        flow_style=event.flow_style
      )
      pending_index = None

    modified_events.append(event)

  with open(output_path, 'w', encoding='utf-8') as f:
    yaml.emit(modified_events, f)
  
  return modified_events

def ankorpin_map():
  input_file = 'sources/app/lstaxizer.yaml'
  output_file = 'sources/app/lstaxizer.yaml_anchored.yaml'

  try:
    final_events = ankorpin_process_and_remap(input_file, output_file)
    print(f"Successfully processed YAML. Output saved to: {output_file}")
    # ANCHOR - replace output file to input file
    with open(input_file, 'w', encoding='utf-8') as f:
      yaml.emit(final_events, f)
    # ANCHOR - delete the temporary output file
    import os
    os.remove(output_file)
  except Exception as e:
    print(f"Error processing YAML: {e}")

if __name__ == "__main__":
  ankorpin_map()