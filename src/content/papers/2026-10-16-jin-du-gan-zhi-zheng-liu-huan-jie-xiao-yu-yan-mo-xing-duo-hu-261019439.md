---
title: Progress-Aware Distillation for Mitigating Stagnation in Small Language Model
  Agents
title_zh: 进度感知蒸馏缓解小语言模型Agent的多轮交互停滞问题
authors:
- Yuanpu Cao
- Saket Sathe
- Hanyu Wang
- Ziyi Yin
- Fenglong Ma
- Jinghui Chen
affiliations:
- The Pennsylvania State University
- Microsoft CoreAI
arxiv_id: '2610.19439'
url: https://arxiv.org/abs/2610.19439
pdf_url: https://arxiv.org/pdf/2610.19439
published: '2026-10-16'
collected: '2026-10-21'
category: Agent
direction: Agent能力蒸馏 · SLM多轮交互优化
tags:
- Agent_Distillation
- SLM
- Progress_Stagnation
- SFT
- LoRA
one_liner: 提出ProD进度感知蒸馏框架，自适应惩罚停滞轨迹，提升SLM Agent任务成功率与执行效率
practical_value: '- 多轮交互类Agent（如电商导购、客服、搜索query多轮改写）蒸馏时，可直接复用本文的lexical停滞分数快速识别无效循环，计算成本极低，无需引入额外大模型即可完成离线的轨迹质量评估

  - 在现有SFT Agent蒸馏流程上叠加ProD训练，仅需在SFT checkpoint基础上微调LoRA权重，即可实现准确率提升4%+、推理token消耗降低20%+，适合业务侧快速迭代落地

  - 对于小参数模型部署的Agent场景，可采用迭代ProD优化策略，多轮蒸馏后能进一步缩小与大模型教师的行为差距，缓解小模型长交互能力不足的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型Agent推理成本高、延迟大，业界普遍通过SFT将大模型Agent能力蒸馏到小语言模型（SLM），但蒸馏后的SLM Agent在长交互轨迹中极易出现进度停滞：反复执行无效策略陷入循环，无法推进任务，且模型越小、轨迹越长问题越严重，成为SLM Agent落地的核心瓶颈。

### 方法关键点
- 定义三类停滞分数量化轨迹停滞程度：lexical重叠（ROUGE-L）、语义相似度（句向量余弦）、LLM-as-judge打分，三类指标相关性达0.92以上，可根据业务成本灵活选择
- 计算学生与教师轨迹的停滞gap，构造自适应margin：停滞越严重、答案错误的学生轨迹惩罚力度越大，避免统一惩罚带来的过校正或校正不足
- 优化目标结合进度感知损失与原SFT损失，避免概率偏移，可迭代执行多轮蒸馏进一步缩小与教师的行为差距

### 关键实验
在8款0.6B-8B参数SLM上验证，覆盖MATH、HotpotQA等6个域内/域外基准，对比基础SFT蒸馏：域内准确率平均提升4.7%，域外准确率平均提升4.9%；交互轮次减少11.6%，token消耗降低20.7%；其中Qwen3-4B在HotpotQA上准确率达70.8%，接近GPT-4.1教师的71.0%水平，效果显著优于解码端重复惩罚、训练数据压缩等现有方案。

### 最值得记住的一句话
SLM Agent蒸馏不能只拟合教师单步行为，还需要对齐其连续推进任务的进度动态，才能从根本上解决长交互的停滞问题。
