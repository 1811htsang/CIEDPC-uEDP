from pydantic import BaseModel, field_validator
from typing import List, Optional, Dict

# LINK - sources/app/lstaxizer.yaml
# NOTE - This file is used to check against lstaxer.vlid

class C_isr_obj(BaseModel): # DEPRECATED - Must be removed
  id: str
  to: str
  sig: str

class C_isr_list_obj(BaseModel): # DEPRECATED - Must be removed
  isr_list: Optional[List[C_isr_obj]] = None
  
# CRITICAL
'''
Thông qua các vòng review và đánh giá thiết kế syntax,
ISR đã được xác định là một tính năng không cần thiết 
và cho phép loại bỏ khỏi μE-LS.
Task đã được assign vào task list để loại bỏ ISR support trong syntax, bao gồm pydantic_model, example của docs, pycdscriptor.
'''

# STUB - OCE Stub for YAML file
'''
outexec:
- name: OCE_ITNLOG_DUMP -> str
  handler: itnlog_dump_handler -> str
  context: NULL -> Optional[str] = None
  state: READY -> str
'''

class C_outexec_obj(BaseModel):
  name: str
  handler: str
  context: Optional[str] = None
  state: str

class C_outexec_list_obj(BaseModel):
  outexec_list: Optional[List[C_outexec_obj]] = None