---
title: Recommendation World Models for Future-State Control
title_zh: 面向未来状态控制的推荐系统世界模型
authors:
- Jinfeng Xu
- Zheyu Chen
- Ziyue Peng
- Jianheng Tang
- Zheng Lin
- Jing Yang
- Puzhen Wu
- Zheng Xing
- Victor C. M. Leung
affiliations:
- The University of British Columbia
- The Hong Kong Polytechnic University
- The Hong Kong University of Science and Technology
- Peking University
- University of Luxemburg
arxiv_id: '2609.30711'
url: https://arxiv.org/abs/2609.30711
pdf_url: https://arxiv.org/pdf/2609.30711
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 序列推荐·未来状态可控优化
tags:
- Sequential Recommendation
- World Model
- Controllable Recommendation
- Slate Optimization
- Closed-loop Control
one_liner: 提出效用锚定的推荐世界模型接口UA-TWM，无需重训排序模型即可兼顾推荐效用与长期状态调控
practical_value: '- 现有成熟排序模型无需重训，可直接外挂UA-TWM控制层实现长期目标调控（比如降低内容集中度、优化品类曝光结构），业务落地成本极低，不影响原有基线效果

  - 候选生成可复用锚点排序结果做局部修改（仅替换少量低贡献item），既降低候选搜索空间，也能保证推荐效用不会出现大幅下跌，适合对稳定性要求高的工业场景

  - 可借鉴三层门控逻辑（效用阈值、目标增益阈值、失败风险预测）做候选过滤，当无符合要求的候选时直接fallback到原有基线，避免不可控的业务损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐模型仅优化短期点击/转化效用，无法感知推荐slate对用户长期状态的影响，相同短期效用的两个slate可能带来完全不同的长期用户兴趣分布、内容消费多样性、复访率等。业务上需要在不损害短期推荐效果的前提下，实现对用户长期状态的定向调控（比如避免信息茧房、引导用户消费新品类、平衡创作者曝光等），但现有可控推荐方法往往需要重训整个排序模型，落地成本高，难以复用现有成熟的排序基线。

### 方法关键点
- 核心设计UA-TWM接口，完全冻结原有排序模型，以其输出的slate为效用锚点，仅在锚点附近生成候选slate（局部修改少量低贡献item、加入目标对齐的候选），大幅降低搜索空间
- 三层候选筛选逻辑：第一关预测候选相对于锚点的效用损失，确保不低于预设阈值；第二关预测候选相对于锚点的目标状态增益，满足调控要求；第三关用L2正则化的逻辑回归模型预测候选的失败风险，过滤高风险候选，无符合要求的候选时直接返回锚点slate
- 支持两种部署模式：离线日志回放模式基于历史数据校准参数，适合冷启动；闭环交互模式基于1步状态转移预测，实时根据用户反馈更新决策，适合在线调控

### 关键实验
在MovieLens-25M、KuaiRand-Pure两个公开数据集上测试12种主流序列推荐backbone（GRU4Rec、SASRec、BERT4Rec、S3Rec等），所有backbone挂载UA-TWM后均获得稳定提升：MovieLens上Recall@20中位数提升5.9%，NDCG@20中位数提升5.9%，未来状态L1损失降低0.037~0.046；KuaiRand上Recall@20中位数提升6.4%，NDCG@20中位数提升6.5%，未来状态L1损失降低0.064~0.082；KuaiSim闭环测试中UA-TWM实现0次无效调控声明，在保留点击效用的同时有效完成目标状态调控。

**最值得记住的一句话**：工业推荐系统的长期目标调控无需重训已验证的成熟排序模型，仅需在其输出层增加局部候选搜索与约束筛选层，即可兼顾短期效果稳定性与长期目标的可控性。
