---
title: 'Drift-Constrained Optimization: Only Direction Matters in Fine-Tuning Instruct
  Models'
title_zh: 漂移约束优化：指令模型微调中更新方向决定最终效果
authors:
- Fei Yuan
- Changjiang Gao
- Yilei Tu
- Yifeng Liu
- Shujian Huang
- Yu Qiao
affiliations:
- Shanghai Artificial Intelligence Laboratory
- National Key Laboratory for Novel Software Technology, Nanjing University
- University of British Columbia
arxiv_id: '2609.13680'
url: https://arxiv.org/abs/2609.13680
pdf_url: https://arxiv.org/pdf/2609.13680
published: '2026-09-11'
collected: '2026-09-16'
category: Training
direction: LLM微调 · 漂移约束与方向选择
tags:
- Fine-Tuning
- Behavioral Drift
- Layer-wise Tuning
- Instruct LLM
- Parameter Efficient Tuning
one_liner: 提出漂移约束下的微调方向选择框架，仅用QA监督即可提升目标任务同时保留模型通用能力
practical_value: '- 做垂域LLM微调（电商客服、商品文案生成、Agent推理模块）时，可优先采用底部+顶部层更新、中间层冻结的分层调优方案，相同行为漂移下目标任务提升更高，还能大幅降低通用能力退化、灾难性遗忘风险

  - 缺少中间监督信号的场景（仅用QA对微调推理模型、仅用点击转化数据微调生成式推荐模型），可复用方向选择思路，无需在损失函数加正则，直接限制更新方向即可平衡目标效果与通用能力

  - 微调后需对接RLHF/RLAIF的场景（如广告推荐的reward对齐），用分层调优方案做初始化，能比普通基模型获得更大的RL提升

  - 冻结lm_head层的trick可直接复用，能减少不必要的行为漂移，提升单位漂移的任务收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有指令模型微调仅优化目标任务损失，无控行为漂移会引发灾难性遗忘、通用能力退化，常规KL正则仅能调整漂移与效果的权衡边际，无法突破固有trade-off上限。

### 方法关键点
- 将微调建模为固定漂移预算下的方向选择问题，基于参考模型Fisher几何构造局部行为坐标系，用径向坐标衡量漂移量级，方向坐标衡量更新分配，定义方向效率指标量化单位漂移的任务收益
- 提出分层选择调优（LST）方案，仅更新Transformer底部k层+顶部m层、冻结中间层，低成本构造高效更新方向族
- 新增lm_head层冻结约束，避免不必要的分布漂移，进一步提升方向效率

### 关键实验
- 数据集：科学推理任务用300K SmolInstruct样本，多语言翻译任务用2.8M Lego-MT样本覆盖100+语言
- 对比基线：全量微调、LoRA、KL正则微调（ASFT），测试模型覆盖Qwen3-8B、Qwen3-14B、InternS1-mini-8B
- 核心结果：仅用QA对监督时，LST在100+语言翻译任务上较Qwen3-8B基线最高提升11.26分，匹配或超越Seed-X-PPO-7B等专用翻译系统；通用能力保留率比全量微调高30%以上，作为RL初始化时较基线RL模型最高额外提升3.79分

固定行为漂移预算下，微调的核心不是参数更新幅度，而是更新方向的选择
