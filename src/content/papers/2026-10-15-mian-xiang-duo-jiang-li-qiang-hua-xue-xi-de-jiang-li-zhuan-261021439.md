---
title: 'Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment
  for Multi-Reward RL'
title_zh: 面向多奖励强化学习的奖励专属Token级信用分配算法MRTPO
authors:
- Skylar Zhai
- Haonan Wang
- Zhining Liu
- Linxin Song
- Xuwei Ding
- Jingcheng Liang
- Jian Kang
affiliations:
- University of Minnesota
- National University of Singapore
- University of Illinois Urbana-Champaign
- University of Southern California
- University of Pennsylvania
arxiv_id: '2610.21439'
url: https://arxiv.org/abs/2610.21439
pdf_url: https://arxiv.org/pdf/2610.21439
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: LLM对齐 · 多奖励RL训练优化
tags:
- RLHF
- Multi-Reward RL
- Credit Assignment
- GRPO
- LLM Alignment
one_liner: 无需额外辅助模型与Token级标注，将各奖励优势分配到对应相关Token，提升多奖励RL性能与收敛速度
practical_value: '- 电商Agent工具调用、生成式推荐商品文案/营销话术生成等多奖励对齐场景，可直接复用MRTPO思路，无需为每个奖励标注相关Token，仅通过自回放即可实现细粒度信用分配，提升生成准确率与收敛速度

  - 现有基于GDPO、SAW的多奖励RL训练管线可无成本叠加MRTPO，仅需增加少量前向传播开销，训练时长仅上升10%~20%，无需修改现有奖励加权逻辑

  - 搜索Query改写、商品评论合规校验等带多个可验证约束的生成任务，可复用留一上下文自回放的方法定位每个约束对应的Token，避免错误惩罚扩散到无关内容，降低误修正概率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多奖励RL对齐方案（如GDPO、SAW）仅在响应层面调整各奖励权重，将优势均匀分配给所有Token，导致局部错误的奖惩被稀释，无关Token被误奖惩，收敛速度慢；现有细粒度Token级信用分配方案依赖额外标注或辅助模型，落地成本高。
### 方法关键点
- 留一上下文构造：对每个奖励的可验证信息（参考结果、执行错误、约束要求等）构造两组上下文，一组包含所有奖励的验证信息，另一组仅移除当前奖励的验证信息
- 自回放相关性计算：用采样响应时的旧策略在两组上下文下回放响应，计算每个Token位置下一词分布的JS距离，作为该Token对当前奖励的相关性得分
- 优势重分配：按相关性得分将每个奖励的组归一化优势加权分配到对应Token，默认β=0.5，即50%的优势按相关性分配，剩余50%均匀分配，保证单响应总奖励和GDPO完全一致
### 关键结果
在文本到SQL、指令跟随、工具调用3类任务6个模型上均优于基线：文本到SQL平均准确率比GDPO高1.3~1.6pp；指令跟随零样本IFBench准确率高2.4~3.2pp；工具调用格式奖励收敛到0.8的步数比GDPO少32%，单步训练耗时仅增加10%~20%，可直接叠加SAW等响应层奖励加权方法进一步提升效果。
> 最值得记住：多奖励RL优化的核心不仅是调整各奖励的权重，更要将每个奖励的奖惩落到真正相关的Token上。
