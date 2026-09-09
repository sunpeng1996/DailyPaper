---
title: 'ThinkPrior: Zero-Rollout Difficulty Priors for Cold-Start Prompt Selection
  in RLVR'
title_zh: ThinkPrior：RLVR冷启动prompt选择的零滚动难度先验方法
authors:
- Tommy Sha
- Skylar Zhai
- Siqi Zhao
affiliations:
- Stony Brook University
- University of Minnesota Twin Cities
arxiv_id: '2609.09075'
url: https://arxiv.org/abs/2609.09075
pdf_url: https://arxiv.org/pdf/2609.09075
published: '2026-09-08'
collected: '2026-09-09'
category: Training
direction: RL训练 · 冷启动prompt选择
tags:
- RLVR
- GRPO
- Cold Start
- Prompt Selection
- Difficulty Prior
one_liner: 无需目标策略滚动，用外部锚离线构造难度先验降低RLVR冷启动无效滚动浪费
practical_value: '- 做LLM RL微调/指令调优的样本冷启动选择时，可复用「小锚模型离线打标+Beta分布初始化先验」思路，无需一开始消耗大模型rollout成本即可初步区分样本难度，降低无效计算

  - 推荐系统新物品/新用户冷启动排序可迁移该框架：用外部离线信号构造初始先验分布，后续再用实时业务数据更新分布参数，避免冷启动阶段纯随机探索的资源浪费

  - 采用GRPO/RLOO等分组相对优势训练时，优先选择模型通过率接近50%的样本，这类样本的梯度信号贡献最高，可有效降低无效训练成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR（带可验证奖励的强化学习）采用GRPO训练时，39%的rollout完全无效：若一个prompt组的所有输出全对或全错，组内相对优势为0，不贡献任何奖励-优势梯度。现有基于历史的prompt选择方法需先运行目标策略的rollout才能估计难度，冷启动阶段浪费大量计算资源，在短周期LoRA训练场景下冷启动开销占比极高。

### 方法关键点
- 离线阶段用小参数量外部锚模型跑通所有候选prompt，用与训练一致的验证器打标，得到每个prompt的离线通过率
- 用锚模型的通过率初始化Beta分布伪计数作为难度先验，全程不需要目标策略的rollout
- 训练阶段每个step按后验期望可学习性（非全对/全错的概率）排序选prompt，选中后用实际rollout结果更新Beta分布参数，不改动原有损失与优化器
- 评分规则自带分散惩罚：相同后验均值下优先选择难度估计更确定的prompt，与不确定性采样逻辑相反

### 关键结果
基于Qwen2.5-Math-7B做LoRA GRPO训练，对比均匀采样、MoPPS、GRESO等基线：16组种子实验下，冷启动前10步的无效组占比从23.8%降至10.6%，相对下降55%；前30步浪费的rollout量下降19%，最终准确率无显著差异。与DAPO结合后，总生成rollout量下降10.6%，最终准确率保持一致，前30步浪费量下降65.4%。仅需1.5B规模的小锚模型即可得到有效的难度先验，无需与目标模型同规模。

### 最值得记住的一句话
GRPO训练中太简单和太难的prompt对梯度的贡献等价为0，冷启动阶段用外部小模型离线构造难度先验就能砍掉一半以上的无效计算，且不影响最终效果。
