---
title: 'You Changed Your Mind, The Model Didn''t: Demystifying Intent in Multi-Turn
  Dialogue'
title_zh: 多轮对话意图识别误区：已否决需求仍干扰模型输出
authors:
- Junle Chen
- Wei Chen
- Zhengjun Huang
- Zhoujin Tian
- Yuxuan Liu
- Kai Wang
- Rui Chen
- Xiaofang Zhou
affiliations:
- HKUST
- Tencent
arxiv_id: '2610.06496'
url: https://arxiv.org/abs/2610.06496
pdf_url: https://arxiv.org/pdf/2610.06496
published: '2026-10-04'
collected: '2026-10-09'
category: LLM
direction: 多轮对话 · 意图对齐与自蒸馏训练
tags:
- Multi-turn Dialogue
- Intent Alignment
- Self-distillation
- LLM Evaluation
- On-policy Training
one_liner: 提出多轮意图评测基准与决策条件自蒸馏框架，缓解已失效意图对模型输出的干扰
practical_value: '- 电商智能客服Agent可复用Intent-OPSD自蒸馏范式，用单轮正确意图监督多轮对话推理，减少用户反复修改需求（如改收货地址后撤回）场景下的回复错误

  - 多轮导购类推荐Agent训练可参考Intent-Eval构造逻辑，生成包含需求澄清、拒绝、修改的多轮对话样本，提升意图跟踪鲁棒性

  - 可直接复用Intent-Eval的评估逻辑，针对业务场景构造多轮意图评测集，量化现有LLM客服/导购的意图识别准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM处理多轮对话时存在严重的意图跟踪偏差：用户明确拒绝的修改提议、已废弃的需求仍会被模型当成有效意图执行，即便用户最终意图未发生变化也会输出错误结果，现有基准缺乏对澄清、接受、拒绝三类意图变更的对照评测，无法系统性量化该问题。

### 方法关键点
- 构造Intent-Eval基准，覆盖工具调用、代码、数据库、数学4个领域共414个任务，设置Original（无变更）、Neutral（仅澄清）、Retained（提议变更被拒）、Revised（提议变更被接受）4种多轮条件，搭配单轮对照任务分离多轮交互干扰
- 提出Intent-OPSD决策条件自蒸馏框架：同架构frozen Teacher接收与用户最终决策匹配的完整单轮任务作为监督信号，Student在完整多轮对话上做On-policy训练，对齐Teacher的token分布，推理时无需Teacher参与

### 关键实验
- 测试8款主流LLM，发现多轮拆分任务比单轮平均准确率降36.30pp，仅添加无关澄清再降4.43pp，提出变更被拒/被接受分别再降8.06/5.55pp，59.63%的被拒场景错误包含已失效内容
- Intent-OPSD在4款模型、4个领域上平均比基线提升10.81pp，比普通SFT提升3.73pp，在工具调用领域增益达21.46pp

### 最值得记住的一句话
多轮对话中LLM普遍存在"提及即生效"的认知误区，必须明确区分对话中提到的内容和最终有效的用户意图
