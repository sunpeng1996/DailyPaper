---
title: 'CoPersona: Collaborative Persona Graphs for Robust LLM Personalization'
title_zh: CoPersona：面向鲁棒LLM个性化的协同人物图谱框架
authors:
- Yangtian Zhang
- Leyao Wang
- Hiren Madhu
- Ngoc Bui
- Walter Roznyatovskiy
- Rex Ying
affiliations:
- Yale University
- Samsung
arxiv_id: '2607.01485'
url: https://arxiv.org/abs/2607.01485
pdf_url: https://arxiv.org/pdf/2607.01485
published: '2026-07-01'
collected: '2026-07-03'
category: LLM
direction: LLM个性化 · 协同用户建模
tags:
- LLM Personalization
- Collaborative Filtering
- Multiplex Graph
- RAG
- Soft Prompt
- GNN
one_liner: 基于分面多路用户相似图与双分支推理，解决LLM个性化的用户历史稀疏与分面覆盖偏差问题
practical_value: '- 可复用分面解耦用户建模思路：将用户历史拆解为偏好、风格、价格敏感度等可解释分面，结合置信度评分过滤低可靠特征，适配电商用户冷启动、行为稀疏场景

  - 多路用户相似图构建方法可迁移到跨用户协同召回：按不同分面分别构建用户关系层，实现定向同好特征迁移，减少全局相似度检索带来的负迁移

  - 双分支推理架构可直接复用在生成式推荐场景：非参数分支的分面级同好特征作为prompt硬输入，参数分支的图聚合结果作为软提示，平衡可解释性与效果，适配个性化文案生成、种草内容生成等业务

  - 实测97%以上用户存在至少一个弱支持分面，业务中做个性化需避免过度依赖已有稀疏行为，优先补全弱支持分面的信号'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM个性化方案高度依赖用户历史交互数据，但真实场景中用户行为普遍存在稀疏性与分面覆盖偏差：大部分用户仅能提供少量交互，且历史仅覆盖偏好、风格等少数维度，当测试请求涉及未观测分面时，现有方法易生成通用内容或幻觉化用户特征，基于全局相似度的同好信号迁移易引入噪声，负迁移风险高。

### 方法关键点
- 分面解耦：从全局用户行为中聚类挖掘领域适配的可解释分面 schema，将每个用户的历史按分面生成文本摘要、置信度评分与对应 embedding，低置信度分面用中性占位符补全
- 多路协同人物图谱构建：每个分面对应一层独立的用户相似图，边权重由分面 embedding 余弦相似度与双方分面置信度共同计算，保留TopK邻居实现稀疏化，支持定向分面信号迁移
- 双分支推理：非参数分支检索分面对齐的同好用户摘要作为硬prompt输入，参数分支通过置信度门控的图消息传递，聚合同好信息补全用户弱支持分面，生成软提示注入LLM
- 联合优化：拼接软提示、用户自历史检索结果、同好检索结果作为LLM输入，端到端微调LoRA与图推理模块

### 关键结果
基于6个亚马逊评论生成数据集实验，7B模型下Books数据集ROUGE-1比SOTA基线DEP高3.3pp，BLEU高3.1pp；LLM-as-Judge评估的内容真实感评分比DEP高0.19分；稀疏交互场景（Video Games）下BLEU增益达1.21pp。数据显示97%以上的用户存在至少一个弱支持分面，验证了分面覆盖偏差的普遍性。

**核心结论**：用户历史的非观测特征不代表不存在，基于分面的跨用户协同补全能显著降低稀疏场景下LLM个性化的负迁移率
