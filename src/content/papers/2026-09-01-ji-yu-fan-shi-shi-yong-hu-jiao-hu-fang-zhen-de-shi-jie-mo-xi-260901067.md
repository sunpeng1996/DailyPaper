---
title: World Model-Guided Reinforcement Learning via Counterfactual User Engagement
  Simulation
title_zh: 基于反事实用户交互仿真的世界模型引导强化学习推荐框架
authors:
- Ang Li
- Xin Xu
- Bin Liang
- Yue Ma
- Fubang Zhao
- Yangyang Kang
- Kam-Fai Wong
affiliations:
- The Chinese University of Hong Kong
- Zhejiang University
- ByteDance China
- MoE Key Lab of High Confidence Software Technologies, CUHK
arxiv_id: '2609.01067'
url: https://arxiv.org/abs/2609.01067
pdf_url: https://arxiv.org/pdf/2609.01067
published: '2026-09-01'
collected: '2026-09-02'
category: GenRec
direction: 生成式推荐 · 世界模型反事实仿真
tags:
- World Model
- Reinforcement Learning
- User Simulation
- Counterfactual Reasoning
- LLM4Rec
- Cross-domain Transfer
one_liner: 训练用户交互世界模型生成反事实奖励，让1.7B小推荐模型效果赶超超大规模LLM
practical_value: '- 可复用UEWM训练范式：基于用户历史异构交互序列做自回归预训练，加轻量CoT推理引导、GRPO奖励对齐，即可得到高保真用户模拟器，规避在线RL的成本、延迟与业务风险

  - 可迁移WMG-RL奖励设计：将点赞/收藏/评分/评论等异构用户反馈按业务目标加权转换为RL奖励，无需人工标注，适配电商/内容推荐/本地生活等不同场景的KPI需求

  - 小模型优化新思路：无需传统SFT蒸馏大模型输出，用冻结的大模型用户模拟器为小模型RL提供同状态反事实对比奖励，1.7B小模型即可达到超大规模LLM效果，大幅降低线上推理成本

  - 跨域落地参考：仅用中文短视频数据训练的UEWM可零-shot迁移到英文电商/本地生活场景，说明用户动态建模的核心逻辑通用，可减少跨域场景的训练数据采集成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐场景下在线RL训练用户侧策略存在核心痛点：在线反馈采集成本高、延迟大、风险高，现有日志仅能记录已曝光的item，无法获得同一用户状态下多个候选item的反事实对比信号，传统监督学习无法满足策略优化的需求。

### 方法关键点
- 构建UEWM（用户交互世界模型）：将推荐item作为Agent动作，用户异构反馈作为环境观测，从用户历史交互中推断个性化动态响应规则，而非训练固定的群体级响应模型
- UEWM三阶段训练：以Qwen3-8B为基座，第一阶段用大规模交互序列做自回归预训练，第二阶段用CoT数据做轻量微调引导模型显性化用户偏好推理，第三阶段用GRPO做奖励校准提升反馈预测准确率
- 提出WMG-RL框架：冻结训练好的UEWM作为代理环境，下游策略在同一用户历史下生成多个候选item，UEWM并行预测每个item的用户反馈，转换为密集 reward 优化策略，实现同一用户状态下的反事实对比

### 关键结果
用2.5M用户、636M条中文短视频交互数据训练UEWM，零-shot跨域测试覆盖Amazon图书/电影、Google本地评论三个公开数据集，对比基线包括Qwen3-235B、OpenAI o3、DeepSeek-R1等超大规模LLM。核心数字：UEWM跨域评分准确率比最优基线高3.9个百分点；WMG-RL训练的1.7B小推荐模型在三个跨域数据集上的推荐准确率分别达41.91%、42.84%、37.95%，超过OpenAI o3等大模型，也比SFT蒸馏、传统奖励模型基线高2~3个百分点。

**最值得记住的一句话**：用户交互世界模型学到的是从历史推断用户动态响应的通用逻辑，而非领域特定的统计特征，可作为低成本反事实奖励源替代在线反馈训练推荐策略。
