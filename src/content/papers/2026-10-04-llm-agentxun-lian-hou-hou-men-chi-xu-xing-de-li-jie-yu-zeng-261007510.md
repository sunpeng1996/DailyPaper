---
title: Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training
title_zh: LLM Agent训练后后门持续性的理解与增强研究
authors:
- Qiusi Zhan
- Nian Lyu
- Stephanie Ding
- Arnav Mehta
- Xander Davies
- Daniel Kang
affiliations:
- University of Illinois Urbana-Champaign
- MATS Research
- Independent Researcher
- University of Oxford
- Measuring AI Progress, Inc.
arxiv_id: '2610.07510'
url: https://arxiv.org/abs/2610.07510
pdf_url: https://arxiv.org/pdf/2610.07510
published: '2026-10-04'
collected: '2026-10-07'
category: Agent
direction: LLM Agent 后门安全与供应链风险
tags:
- Backdoor
- LLM Agent
- SFT
- RL
- Supply Chain Risk
one_liner: 发现RL会保留甚至强化SFT后残留的LLM Agent后门，提出PersistBD大幅提升后门持续性
practical_value: '- 业务侧使用第三方预训练模型定制Agent时，需补充后门检测环节，尤其在SFT后、RL训练后分别做触发词校验，规避供应链风险

  - 做模型安全防护时，可反向参考PersistBD的两个核心优化维度（初始后门强度、梯度兼容性），针对性设计后门消融策略

  - 针对Agent SFT+RL的训练范式，可复用论文的后门留存率评测方法，自建业务场景下的模型安全评估pipeline'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM Agent多基于第三方预训练模型经SFT、RL二次训练落地，供应链层面存在预训练模型被植入后门的风险，业界对后门在二次训练后的留存规律缺乏系统认知。
### 方法关键点
1. 验证良性SFT会大幅降低后门攻击成功率（ASR），但后续RL训练往往保留残留后门，甚至提升ASR；
2. 提炼出影响后门留存的两个核心因素：初始后门强度、后门梯度与良性训练梯度的兼容性；
3. 基于上述因素提出PersistBD，对预植入后门的模型提前优化，提升其经业务二次训练后的后门留存率。
### 关键结果
在Qwen2.5-Coder-7B上，PersistBD将SFT后的ASR从20%提升至74%，SFT+RL全流程后的ASR从20%提升至76%，同时模型良性任务性能无明显下降。
