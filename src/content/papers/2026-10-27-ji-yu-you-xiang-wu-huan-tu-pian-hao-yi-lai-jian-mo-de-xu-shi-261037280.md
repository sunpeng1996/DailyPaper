---
title: Modeling Preference Dependencies with Directed Acyclic Graphs for Narrative-Driven
  Recommendation
title_zh: 基于有向无环图偏好依赖建模的叙事驱动推荐方法
authors:
- Mingzhe Lu
- Jian Qin
- Ruize Qin
- Jinhao Liu
- Yunpeng Li
- Hang Su
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- University of Chinese Academy of Sciences, School of Cyber Security
- The University of Melbourne, Faculty of Engineering and IT
- Independent Researcher
arxiv_id: '2610.37280'
url: https://arxiv.org/abs/2610.37280
pdf_url: https://arxiv.org/pdf/2610.37280
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 偏好依赖建模
tags:
- Narrative-Driven Recommendation
- Preference Dependency Graph
- LLM4Rec
- Directed Acyclic Graph
- Retrieval-Augmented Recommendation
one_liner: 构造偏好依赖有向无环图指导检索排序，大幅提升叙事驱动推荐性能
practical_value: '- 可复用长文本偏好解析逻辑：针对电商用户咨询、内容社区找货等长query场景，先拆分偏好原子再判断层级修饰关系，避免混淆独立偏好与约束关系，大幅提升需求理解准确率

  - 定向路径检索方法可直接迁移：基于偏好依赖边生成组合检索query，而非零散关键词检索，能提升长尾/小众item的召回覆盖率，比仅用原始query召回多2~3倍相关候选

  - 拓扑路径排序方案低本高效：按偏好依赖距离给上游偏好打折扣聚合得分，无需依赖LLM做listwise重排，规避上下文窗口限制、位置偏差问题，推理成本降低80%以上

  - 垂域选型参考结论：在LLM训练数据覆盖度低的垂直品类（小众图书、潮玩、非遗商品等），结构指导的检索增强推荐效果远好于直接调用LLM生成推荐'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有叙事驱动推荐方法普遍将用户输入的自由文本需求视为扁平关键词集合或无约束生成query，忽略了偏好之间的层级修饰、条件约束关系，极易召回仅表面匹配的item，例如用户要「爱情作为副线的奇幻电影」，常召回爱情作为主线的作品，匹配准确率低，且无法处理复杂多约束的长文本需求。
### 方法关键点
1. 用PDG-Agent解析用户叙事：先抽取偏好原子，拆分为「解读维度+具体实例」两层离散节点；
2. 判断节点间的修饰依赖关系生成有向边，消环去冗余后得到偏好依赖DAG，按拓扑序生成每个节点的上下文感知偏好描述；
3. 基于DAG的每条边生成组合检索query，做定向路径检索，从公开Web获取候选item与对应佐证证据；
4. 沿拓扑路径聚合匹配得分，下游偏好权重更高，上游偏好按距离打γ折扣，无需LLM listwise重排即可生成最终排序。
### 关键实验
实验覆盖英文电影、英文图书、中文动漫3个跨语言跨域数据集，对比OCG-Agent、GPT-6-Astra、Perplexity AI等SOTA基线：带年份过滤的PDG-F在电影域P@10/R@10/NDCG@10分别较最优基线提升13.7%/14.1%/19.6%，图书域P@10提升92.4%，动漫域R@10提升60.9%；候选池相关item覆盖率是基线的2~3倍。
### 最值得记住的一句话
叙事类推荐中用户偏好不是独立扁平集合，而是有层级修饰关系的结构，显式建模这种依赖关系能同时突破召回天花板、提升排序准确率。
