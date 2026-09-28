---
title: 'AgentRecommender: LLM Agents Enable Customizable Recommender Systems on the
  User Side'
title_zh: AgentRecommender：基于LLM Agent的用户端可定制推荐系统
authors:
- Ryoma Sato
affiliations:
- National Institute of Informatics
arxiv_id: '2609.31166'
url: https://arxiv.org/abs/2609.31166
pdf_url: https://arxiv.org/pdf/2609.31166
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: 用户侧推荐 · LLM Agent 定制化
tags:
- LLM-Agent
- User-Side-RecSys
- Customizable-Recommendation
- Fair-Rec
- Diversity-Optimization
one_liner: 基于LLM Agent实现无额外标注的用户侧可定制推荐系统，规避平台推荐的利益偏向
practical_value: '- 可复用「基于平台公开推荐结果做二次扩展+重排」的架构，在用户端/端侧实现个性化可控推荐，无需依赖平台后台数据

  - 针对需要多样性/公平性约束的推荐场景，可直接用LLM Agent零样本估计item属性（如价格区间、品类、发布时间），省去人工标注成本

  - 性能随扩展预算B提升，实际业务中可按 latency 要求灵活设置B值，B=1即可超过原生重排效果，性价比极高

  - 端侧部署时可结合localstorage缓存历史推荐结果，完全消除在线请求开销，适配浏览器/客户端低延迟需求'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统平台侧推荐系统以平台利益（GMV、用户停留时长）为核心优化目标，易引发点击诱饵、信息茧房、内容偏向、公平性缺失等问题，损害用户权益。现有用户侧推荐方案高度依赖平台公开的item属性标签，当平台不提供对应标注时，普通用户无法自行构建符合自身需求的推荐系统，落地门槛极高。

### 方法关键点
- 仅基于平台公开的黑盒item-to-item推荐接口（如亚马逊的“买了又买”、YouTube的“即将播放”）获取数据，无需访问平台内部日志、全量item库等核心权限
- LLM Agent执行两阶段流程：① 多轮候选扩展：每轮从当前候选池选择最有助于满足约束的item，调用平台推荐接口扩展候选集，总请求数控制在预算B以内；② 最终筛选：从积累的候选池中挑选K个符合用户自定义约束（如价格平衡、品类覆盖、年代均衡）的结果
- 利用LLM内置世界知识零样本估计item属性，也可结合搜索工具提升属性识别准确率，无需额外标注数据

### 关键实验
在MovieLens 1M（电影）、LastFM（音乐）、Amazon家居电商三个数据集测试，对比平台原生推荐、iAgent（仅重排原生结果）基线：① 电影年代平衡任务成功率从0提升至0.68；② 电影品类覆盖率从5.51提升至8.94（+62%）；③ 音乐品类覆盖率从2.5提升至4.34（+74%）；④ 电商价格平衡任务成功率从0.16提升至0.64（+300%）。B=1时性能即大幅超过基线，随B增大性能进一步上升。

### 核心结论
用户侧可控推荐不需要平台配合改造，仅基于公开推荐接口+LLM Agent即可落地，是打破平台推荐利益偏向的低成本可行路径
