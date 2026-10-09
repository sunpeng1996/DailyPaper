---
title: 'SanSi: A Looped Typed Decision Model for System 1.5 Thinking'
title_zh: SanSi：面向System 1.5思考的循环式类型化决策模型
authors:
- Shuyu Gan
- Young-Jun Lee
- Dongyeop Kang
affiliations:
- University of Minnesota
arxiv_id: '2610.07730'
url: https://arxiv.org/abs/2610.07730
pdf_url: https://arxiv.org/pdf/2610.07730
published: '2026-10-05'
collected: '2026-10-09'
category: Reasoning
direction: LLM 隐式循环推理决策优化
tags:
- Looped-LLM
- System1.5-Reasoning
- Typed-Decision
- LoRA
- Calibration
- Reward-Model
one_liner: 基于预训练循环LM构建多轮隐式推理决策模型，小参数接近3倍参数单通模型精度
practical_value: '- 电商/广告实时分类场景（内容审核、意图判断、广告合规）可复用该架构，小参数模型循环3次即可拿到88%的最大精度增益，平衡精度与
  latency，无需盲目堆大模型参数

  - 做生成式推荐/文案生成的RLHF奖励模型时，用多轮循环输出作为奖励信号，比单通模型质量更高，可提升生成器F1 7.7个点

  - 置信度校准trick：平均多轮循环的输出概率，无需额外训练即可将ECE降低一半，适合推荐中需要置信度分级处置的场景（低置信度转人工）

  - 多步推理场景（用户多轮意图理解、商品规则校验），循环模型比同参数单通模型推理深度更强，可泛化到训练未覆盖的推理长度，性价比高于堆参数'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统类型化决策模型采用单通前向传播（System 1思考），速度快但在多步推理、长文档、知识问答等复杂场景精度差；生成式推理（System 2思考）精度高但延迟高，还破坏了直接输出选项概率的接口，缺乏平衡精度、参数成本、延迟的中间方案。
### 方法关键点
- 以预训练循环LM Ouro为基座，冻结主干参数仅训练LoRA适配器和每轮循环的readout头，总新增参数量仅61M
- 每轮循环后均输出选项概率，采用交叉熵+Brier评分规则联合训练所有轮次的损失，支持1~8轮任意推理预算的自适应切换
- 无需生成中间token，完全通过隐式迭代更新隐状态，保留类型化决策直接输出概率的接口，无需后处理
### 关键结果
实验覆盖6类任务共10027个测试样本，对比同架构单通模型SmolLM2-1.7B、3倍参数单通模型Qwen3.5-4B等基线：
- 8轮循环的SanSi-1.4B精度达72.0%，比同参数单通模型高13.5个百分点，仅比3倍参数的Qwen3.5-4B低1.8个百分点
- 3轮循环即可拿到88%的最大精度增益，多步推理任务上比Qwen3.5-4B高20+个百分点，可泛化到训练未见过的推理长度
- 作为RL唯一奖励信号时，可提升生成器F1 7.7个百分点
> 最值得记住：循环推理是用计算换参数的高性价比方案，3次循环即可拿到绝大多数收益，适配成本敏感的工业级决策场景
