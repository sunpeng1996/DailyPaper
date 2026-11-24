---
title: 'PROSPER: LLMs as Sparse Retrievers for First-Stage Product Search'
title_zh: PROSPER：面向电商商品首阶段搜索的LLM稀疏检索框架
authors:
- Hongru Song
- Yu-An Liu
- Ruqing Zhang
- Jiafeng Guo
- Maarten de Rijke
- Sen Li
- Wenjun Peng
- Fuyu Lv
- Xueqi Cheng
affiliations:
- 中国科学院计算技术研究所
- University of Amsterdam
- 阿里巴巴淘宝天猫集团
- 中国科学院大学
arxiv_id: '2611.28645'
url: https://arxiv.org/abs/2611.28645
pdf_url: https://arxiv.org/pdf/2611.28645
published: '2026-11-21'
collected: '2026-11-24'
category: RecSys
direction: 电商搜索召回 · LLM稀疏检索
tags:
- Sparse Retrieval
- Product Search
- LLM4Rec
- First-stage Retrieval
- Contrastive Learning
one_liner: 提出保留字面保真度的LLM稀疏检索框架，淘宝线上实测GMV提升1.60%
practical_value: '- 做LLM-based稀疏检索时可直接复用Literal Residual Network(LRN)设计，通过残差补偿机制强化品牌、型号等关键字面术语权重，避免LLM语义扩展引入的噪声hallucination

  - 训练阶段可引入Lexical Focusing Window(LFW)：训练早期用固定top-k选择机制强制稀疏化，加速模型收敛，后续用FLOPS正则化微调术语权重，实测比动态窗口效果更优

  - 相似度计算时仅对Query侧做L2归一化，既可以促进Query的稀疏化、压制通用无区分度术语，又能保留Item侧多属性的权重覆盖，兼顾召回精度与召回率

  - 工业部署时可选择1.5B左右的中小尺寸LLM做稀疏检索backbone，实测7B以上模型无明显性能增益，1.5B模型的索引大小仅为同级别稠密检索的61%，满足线上latency要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商首阶段检索要求高召回、低延迟、可解释，稀疏检索因支持倒排索引、可解释性强一直是工业系统核心组件，但传统SPLADE等方案存在词汇不匹配问题；直接用LLM做稀疏检索会出现两大痛点：一是语义扩展易稀释品牌、型号等关键字面信号，二是LLM大词汇量导致训练不稳定、收敛慢，无法适配电商短Query、短标题的搜索场景。
### 方法关键点
- 设计**Literal Residual Network(LRN)**：对LLM输出的基础语义表示做残差补偿，仅对Query/Item中的字面术语位置添加权重补偿，锚定关键实体不被扩展噪声覆盖
- 引入**Lexical Focusing Window(LFW)**：训练早期当表示非零维度超过阈值时，仅保留top-k最高权重的术语强制快速稀疏化，训练后期自动失活，配合FLOPS正则化微调术语权重
- 相似度计算仅对Query侧做L2归一化，既促进Query稀疏化、压制通用无区分度术语，又保留Item侧多属性的权重覆盖
### 关键实验
离线在公开Multi-CPR电商数据集、淘宝107万真实点击数据集上测试，对比BM25、SPLADE-v2、Qwen-based SPLADE、BGE稠密检索等基线；Multi-CPR上Hit@1000达93.9%，较BM25、SPLADE-v2、LLM稀疏检索基线分别提升10.2、4.3、1.5个百分点。线上A/B测试在淘宝8000万商品场景部署1.5B Qwen backbone的PROSPER，直接引导场景净GMV提升1.60%，净交易提升0.31%，净UV提升0.24%；索引大小仅为同级别稠密检索的61%，匹配latency ~20ms满足线上要求。
### 核心结论
电商搜索场景中字面术语是精度的核心保障，语义扩展仅用于补充召回，LLM稀疏检索必须优先保留字面保真度才能实现业务增益。
