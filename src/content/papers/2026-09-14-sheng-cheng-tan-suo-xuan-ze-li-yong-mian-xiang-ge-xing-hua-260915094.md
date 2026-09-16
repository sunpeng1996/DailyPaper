---
title: 'Generate to Explore, Select to Exploit: Aligning LLM-based Headline Generation
  with Personalized Recommendation'
title_zh: 生成探索-选择利用：面向个性化推荐的LLM标题生成对齐框架
authors:
- Yi Chen
- Rufeng Cheng
- Qiang Xie
- Tao Li
affiliations:
- Baidu Inc.
arxiv_id: '2609.15094'
url: https://arxiv.org/abs/2609.15094
pdf_url: https://arxiv.org/pdf/2609.15094
published: '2026-09-14'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐·个性化展示文案生成
tags:
- LLM4Rec
- Personalized Generation
- GSPO
- RLHF
- CTR Optimization
one_liner: 提出解耦探索与利用的GESE标题生成框架，在亿级DAU推荐场景实现CTR+2.57%、停留时长+0.87%
practical_value: '- 可复用「生成探索+选择利用」的解耦架构解决生成式文案场景的mode collapse问题，LLM仅负责覆盖潜在用户兴趣，选择层用实时用户信号做个性化匹配，比端到端生成稳定性更强、落地门槛更低

  - 生成模型训练可套用GSPO+分层奖励机制，分层奖励需同时覆盖CTR收益、内容合规性、候选集多样性三个维度，既避免reward hacking，又通过组内归一化天然强制生成多样性，比多次采样推理成本降低K倍

  - 新生成文案冷启动可采用置信度感知汤普森采样策略，通过预设统计阈值动态终止探索，平衡探索收益与流量风险，适配工业级高流量场景的灰度放量要求

  - 可训练LLM单pass输出多候选的能力，相比多次调用LLM采样的方案，推理成本与 latency 显著降低，适配推荐系统低延迟在线服务要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐场景下单个静态item标题无法覆盖用户多元兴趣，尤其会抑制长尾用户需求。传统端到端训练LLM生成单一最优标题的方案属于点估计优化，容易出现mode collapse，输出泛化的平庸文案，无法应对用户画像噪声和兴趣多模态的问题，长期会降低用户engagement。

### 方法关键点
- 架构解耦为离线生成探索、在线选择利用两个阶段：生成阶段用LLM输出覆盖多兴趣的标题候选集，选择阶段用实时信号为用户匹配合适的标题
- 生成端采用三阶段训练：SFT阶段训练模型单pass输出K个候选，降低推理成本；训练融合语义特征和展示特征的CTR奖励模型，用GSPO做RL训练，分层奖励同时兼顾单条标题的CTR、真实性、新颖性，以及候选集的整体多样性
- 选择端冷启动用置信度感知汤普森采样，通过统计阈值动态终止探索，控制探索风险；成熟阶段用DNN排序模型，融合用户画像、实时兴趣、候选语义特征做精细化个性化匹配

### 关键实验
在百度亿级DAU的信息流场景做A/B测试，对比原始静态标题、SFT生成+UCB选择、GSPO生成+UCB选择等baseline，完整GESE框架实现CTR提升2.57%，有效曝光提升0.79%，用户停留时长提升0.87%；离线测试在MSR-50k数据集上，相比SFT baseline，Self-BLEU降低45%，多样性指标和CTR预测得分均优于10倍参数规模的大模型。

### 核心结论
生成式内容与推荐系统对齐的核心不是让LLM输出唯一最优解，而是通过多样性生成对冲用户画像的不确定性，再通过个性化选择实现收益最大化。
