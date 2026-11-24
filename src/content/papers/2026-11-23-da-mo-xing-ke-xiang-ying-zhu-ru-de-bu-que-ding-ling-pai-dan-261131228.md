---
title: Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor
  In Situ
title_zh: 大模型可响应注入的不确定令牌，但无法原位自监测推理错误
authors:
- Daniel Theron
arxiv_id: '2611.31228'
url: https://arxiv.org/abs/2611.31228
pdf_url: https://arxiv.org/pdf/2611.31228
published: '2026-11-23'
collected: '2026-11-24'
category: Reasoning
direction: LLM推理自监测 · 不确定信号纠错
tags:
- LLM Reasoning
- Self-Correction
- In-Situ Monitoring
- Uncertainty Injection
- Chain-of-Thought
- Process Reward Model
one_liner: 证实LLM自校正瓶颈为原位错误检测而非下游修复，可被外部不确定信号引导纠错
practical_value: '- 搭建Agent推理链路时，完全弃用LLM生成时自带的自评估置信度作为剪枝/回溯触发条件，其错误识别AUROC接近随机，会引入不可控噪声，必须外接独立PRM做步骤级错误检测

  - 推理纠错无需构造复杂的错误诊断提示，仅在PRM判定的错误步骤后注入低置信度标签+简单重思考规则，即可达到接近显式错误提示的效果，最高可提38.5%纠错率，大幅降低工程成本

  - 外接PRM需适配基座模型设置精度阈值：Qwen/Phi-4等抗干扰强的模型，PRM精度≥20%-35%即可带来净收益；Llama/Mistral等敏感模型需≥56%-81%精度，多步推理场景要严格控制单步误报率避免累积损失

  - 电商导购Agent、复杂活动规则计算、长Query语义理解等多步推理场景，可直接复用「外接PRM检错+注入低置信度触发重思考」的架构，平衡效果与落地成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Chain-of-Thought、Tree-of-Thought等Agent推理框架普遍依赖LLM生成时口头输出的步骤置信度触发回溯、剪枝，但自校正失败的核心瓶颈始终不明确：是LLM无法原位检测到错误，还是检测到错误后不具备修复能力？该问题的结论直接决定了推理链路的架构设计方向，具备极高的工程指导价值。
### 方法关键点
- 测试4款主流开源指令微调模型：Qwen2.5-7B-Instruct、Llama-3.1-8B-Instruct、Mistral-7B-Instruct-v0.3、Phi-4 14.7B
- 两阶段实验设计：第一阶段要求模型每步输出单步置信度+全局路径置信度，用Claude Opus 5.5做盲态步骤级错误标注，排除自评估对标注的干扰；第二阶段做反事实干预，在错误步骤处注入不同等级的合成置信度标签，测试下游修复能力
- 样本控制：仅选用模型能力边界内的问题（同一问题模型至少做对过1次），排除因不会做导致的修复失败
### 关键结果
- 原位自监测能力近乎失效：4款模型的步骤级错误识别AUROC仅0.500~0.561，接近随机；出现首个错误时模型输出的全局置信度仍高达95.1%~99.9%，仅不到9%的错误会触发≥10个百分点的置信度下降
- 对外部不确定信号响应显著：在错误步骤注入10%低置信度标签，纠错率比注入95%高置信度提升3.7~22.5个百分点，搭配主动重思考规则最高可达38.5%的纠错率，效果接近显式提示错误位置的正对照
- 误判成本差异极大：给正确步骤注入低置信度会导致正确率最高下降22.8个百分点，不同模型对误判的耐受度相差3~4倍
### 核心结论
LLM自校正的核心瓶颈是原位错误检测，而非下游修复能力，依赖LLM自评估的推理剪枝逻辑本质是在过滤噪声，外接检测+注入不确定信号触发修复是更可靠的工程路径
