---
title: 'NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware
  N-gram Speculative Decoding'
title_zh: NgramRL：基于滚动感知N-gram猜测解码加速RL后训练结构化生成
authors:
- Nilesh Prasad Pandey
- Jangseon Park
- Jason Kong
- Onat Gungor
- Tajana Rosing
affiliations:
- University of California San Diego
- West Virginia University
arxiv_id: '2610.32881'
url: https://arxiv.org/abs/2610.32881
pdf_url: https://arxiv.org/pdf/2610.32881
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: LLM训练优化 · 猜测解码提速RL后训练
tags:
- Speculative Decoding
- RL Post-Training
- N-gram Cache
- CPU-GPU Co-design
- LLM Acceleration
one_liner: 基于历史rollout构建无辅助模型的n-gram猜测解码器，最高实现RL后训练rollout 1.38倍加速
practical_value: '- 做生成式推荐/Agent工具调用/结构化输出的LLM RL微调时，可复用per-prompt n-gram缓存方案，无需额外GPU显存，自动对齐迭代中的policy，避免传统猜测解码drafter过时的问题

  - 结构化生成场景（如商品文案、SQL、API参数生成）优先选用per-prompt缓存而非全局缓存，可提升draft接受率20%以上

  - 工程侧可借鉴自适应扇出预取思路，将CPU侧缓存查询、任务调度与GPU前向推理并行，消除CPU-GPU同步空转开销，无需修改模型逻辑即可提升吞吐量'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
RL后训练（尤其是GRPO）的rollout生成阶段占总训练时长70%以上，是主要成本瓶颈。现有猜测解码方案存在三大缺陷：基于辅助模型的drafter额外占用GPU显存，且会随policy迭代逐渐失配；无模型drafter无法利用训练中同prompt跨epoch的输出重复特性，接受率极低，难以落地。
### 方法关键点
- 利用GRPO训练中同prompt跨epoch输出重复度随训练推进逐步升高的特性，为每个prompt单独构建n-gram缓存，仅保留最近W步的rollout数据，自动对齐最新policy，无额外参数、无辅助模型、不占用GPU显存
- 沿用标准猜测验证流程，完全保留原policy的输出分布，不影响训练收敛性和最终模型效果
- 设计自适应扇出预取器，在GPU执行验证的同时预取下一步所有可能验证结果对应的draft，CPU工作与GPU计算完全并行，消除同步空转，预取未命中时自动回退到同步查询，不改变输出结果
### 关键实验
在Qwen3-8B、DeepSeek-7B两个开源模型，GSM8K、Spider、CodeContests三个数据集上测试，对比PLD、REST、SuffixDecoding三个无模型基线：暖缓存状态下每步提交3.60~7.77个token，比SuffixDecoding最高提升1.99倍，比PLD最高提升7.0倍；Spider任务上预取器在候选预算为16时覆盖率达96.6%，rollout吞吐量比同步版本提升1.38倍，接近1.40倍的理论上限。
### 核心结论
RL后训练中同prompt的历史rollout是免费的高质量猜测解码草稿源，无需额外模型即可实现无损加速。
