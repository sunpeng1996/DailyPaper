---
title: 'PinEqualizer: Full Funnel Content Exploration and Debiasing System at Pinterest'
title_zh: 'PinEqualizer: Pinterest全链路内容探索与去偏系统'
authors:
- Olafur Gudmundsson
- Bo Zhao
- Huayi Liao
- Anna Kiyantseva
- Sai Xiao
- Heath Vinicombe
- Mostafa Keikha
- Luke DeLuccia
- Zihao Chen
- Junpeng Hou
affiliations:
- Pinterest, Inc.
arxiv_id: '2607.22518'
url: https://arxiv.org/abs/2607.22518
pdf_url: https://arxiv.org/pdf/2607.22518
published: '2026-07-24'
collected: '2026-07-27'
category: RecSys
direction: 推荐系统 · 全链路冷启动去偏
tags:
- Cold-Start
- Debiasing
- Full-Funnel-RecSys
- Multi-Armed-Bandit
- Ecosystem-Health
one_liner: 覆盖全链路的内容冷启动去偏系统，落地Pinterest后大幅提升新内容曝光与生态健康
practical_value: '- 冷启动治理先做全链路瓶颈分析，按「输入新鲜内容占比/输出留存率」定位卡脖子阶段，优先解决上层（语料/召回）瓶颈再优化排序，避免无效投入

  - 排序模型去偏可复用trick：对item历史统计特征做独立dropout，引入Semantic ID、纯内容embedding（如VLM特征）做补充，缺失特征按语料分布采样补全，不影响用户侧个性化

  - 探索机制可复用分层策略：上层召回单独建冷启动内容的倒排/ANN索引保障流量供给，排序层结合UCB做探索，搜索场景下探索权重与内容相关性挂钩，避免破坏用户体验

  - 冷启动效果评估可复用三层指标体系：长期用新内容holdout实验测用户增量价值，中期用内容毕业率做代理指标，短期用未充分探索内容的正向互动量做A/B实验指标，兼顾迭代效率和长期收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级搜索推荐系统普遍存在内容冷启动问题，Pinterest传统依赖的Pin-board图结构对未建立关联的新增内容极不友好，马太效应显著，既限制新创作者成长，也损害长期内容生态健康和用户体验；传统冷启动方案多聚焦单阶段优化，缺乏全链路协同的去偏方案，且没有兼顾短期迭代效率和长期价值的标准化评估体系。
### 方法关键点
- 全链路协同优化：覆盖语料选择、召回、排序、效用层全阶段，语料层用Thompson采样+模型先验筛选高潜力新内容构建专属探索语料；召回层为冷启动内容单独建立倒排/ANN索引，修改图遍历权重提升新内容召回占比；排序层通过纯内容embedding补充、item历史特征独立dropout、DCNv2特征交叉、近实时特征接入消除对旧内容的偏好；效用层结合印象数启发式UCB/Neural Linear UCB做探索，搜索场景下探索权重与内容相关性挂钩避免破坏体验
- 三层评估体系：长期用新内容holdout实验（对照组等量随机删除内容消除候选池优势）测新增内容的用户增量价值，中期用内容毕业率（Y天内获得X次正向互动）做代理指标，短期用未充分探索内容的正向互动量做A/B实验指标，解决传统A/B的内容泄露问题
### 关键实验
落地Pinterest三大核心场景（Homefeed、搜索、Related Pins，占总曝光92%），2025年较2024年：新内容带来的北美整体成功会话提升24%、北美购物会话提升63%，28天内毕业的内容量提升41%，成功内容创作者数提升99%，未充分探索内容互动量在Homefeed/搜索/Related Pins分别提升37%/13%/27%
### 核心结论
冷启动治理不能只靠单阶段探索，全链路去偏+分层指标体系才能兼顾短期用户体验和长期生态价值
