---
title: Which Rollout Taught It That? BehaviorTrace and the Limits of Training-Data
  Attribution in Online RL
title_zh: 在线RL训练数据归因的局限性与BehaviorTrace评测基准
authors:
- Amit Nautiyal
affiliations:
- Independent Researcher
arxiv_id: '2610.10422'
url: https://arxiv.org/abs/2610.10422
pdf_url: https://arxiv.org/pdf/2610.10422
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: LLM RL微调 · 训练数据归因评测
tags:
- ReinforcementLearning
- DataAttribution
- GRPO
- EvaluationHarness
- LLMFinetuning
one_liner: 开源在线RL训练数据归因评测基准BehaviorTrace，揭示主流梯度归因方法的混淆与不稳定性
practical_value: '- 业务中用RL微调LLM生成推荐文案、Agent决策时，排查异常行为归因必须增设梯度大小、生成流畅度两个基线对照，避免把梯度大小、流畅度的相关信号错当成行为归因信号

  - 做RL微调后的行为归因时，不要使用构造的续写目标梯度，必须用行为实际出现的上下文in-context梯度，否则结果会出现反向误导

  - 定位RL微调引入的特定输出行为时，优先做token级梯度对齐，不要使用整条回复的梯度，后者的有效信号会被无关内容完全淹没

  - 验证或自研归因方法可直接复用BehaviorTrace的6项检查清单，规避梯度参数覆盖不全、单跑结果不稳定等结构性陷阱'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RL微调（如GRPO做RLHF）常使LLM学到预期外的异常行为，梯度归因是定位问题训练样本的主流手段，但这类方法此前仅在监督静态场景验证，在线RL微调场景下的有效性未经过严格校验，结果可信度存疑。
### 方法关键点
- 构造可控植入行为实验：先通过10条SFT样本给Qwen2.5-1.5B植入`frobnitz→QZXBT`触发关联，再用GRPO微调，前200步给符合触发行为的rollout加额外奖励，得到已知ground truth的污染样本集
- 开源BehaviorTrace评测基准，整合全梯度CountSketch压缩、植入行为实验范式，内置梯度大小、流畅度、多种子多生成采样等对照控制
- 对比GAS、TRAK-style、TracInCP三类主流梯度归因方法，以及无目标梯度大小排序、随机排序等基线
### 关键结果
- 步级归因：无目标的梯度大小控制组精度达随机的4.2~4.5倍，在2/3种子上匹配甚至超过最优的有目标归因方法
- Rollout级归因：控制流畅度后，归因结果在不同种子、不同生成采样下完全不稳定，无稳定胜出的归因方法
- 仅token级信号稳定：触发词的梯度与实际上下文目标梯度的对齐度在所有种子上显著高于随机，全回复梯度无有效信号
### 核心结论
在线RL微调场景下的单run归因结果完全不可靠，必须通过多种子、多采样、加混淆因子对照才能保证结果可信度
