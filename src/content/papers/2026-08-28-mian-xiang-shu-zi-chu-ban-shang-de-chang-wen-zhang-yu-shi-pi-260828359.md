---
title: 'Every Article Deserves a Video: Contextual Video Matching for Digital Publishers'
title_zh: 面向数字出版商的长文章与视频上下文匹配系统
authors:
- Arnaud Corone
- Brice Pierre de la Briere
- Gladys Roch
- Samuel Leonardo Gracio
- Yassine Bouher
- Parvati Chauchaix
affiliations:
- Dailymotion
arxiv_id: '2608.28359'
url: https://arxiv.org/abs/2608.28359
pdf_url: https://arxiv.org/pdf/2608.28359
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 跨模态内容推荐 · LLM增强检索
tags:
- Video Recommendation
- HyDE
- LLM4Rec
- Embedding Retrieval
- LLM-as-a-Judge
one_liner: 结合LLM与HyDE框架实现长文与视频规模化自动匹配，上线后大幅提升用户参与度与平台收入
practical_value: '- 存量embedding模型无法替换时，可通过LLM生成新兴实体的grounding描述，无需重训模型即可弥补旧模型的知识缺口，提升检索精度

  - 可将HyDE框架迁移到跨模态匹配场景：将长文本（如商品详情页、资讯）转换为待匹配侧的统一元数据格式，拉齐语义空间以提升匹配效果

  - 缓存LLM生成的中间语义表示而非最终推荐结果，既降低推理成本与 latency，又能动态适配新增候选池（如新上线的视频、商品），适合静态查询、候选动态更新的场景

  - 可按不同商家/业务线的内容语义分布动态设置相似度阈值，避免一刀切的精度损失，同时支持业务方手动调整阈值适配自身标准'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
数字出版商为图文内容匹配相关视频可显著提升视频广告CPM、延长页面停留时长优化SEO，但人工匹配操作成本高无法规模化，现有视频-文本匹配方案多针对短文本设计，无法适配长文章的语义匹配需求。

### 方法关键点
- 采用多阶段pipeline：先用Gemini LLM过滤HTML噪音，生成与视频元数据格式对齐的假设性内容（HyDE），同时提取文章语言、新兴实体的grounding描述，弥补存量MUSE模型的知识缺口
- 统一使用MUSE编码文章假设内容与视频元数据，基于Qdrant做ANN检索，支持按语言、publisher ID、发布时间预过滤，根据每个publisher的内容语义分布动态设置相似度阈值，混合cosine相似度与视频新鲜度排序
- 评估采用LLM-as-a-Judge方案，结合主题相关性+用户意图双维度打分、Chain-of-Thought推理与Bradley-Terry pairwise对比，解决无标注长文-视频匹配数据的评估难题

### 关键结果
离线评测基于1032个真实出版商页面，相比基础HTML解析基线，高分匹配（得分≥4）占比从15.5%提升至19.9%，Bradley-Terry评分达1666，显著优于所有基线；线上A/B测试相比随机匹配基线，人均观看时长提升19%，单观看平均时长提升21%。目前系统已覆盖200+出版商，贡献Dailymotion 2%-3%的出版商侧收入。

最值得记住的一句话：工业落地中，适配现有基础设施的优化，往往比盲目替换新模型的投入产出比高得多。
