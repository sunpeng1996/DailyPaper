---
title: 'FieldGuideRAG: Image-Grounded GraphRAG for Fine-Grained Recognition with Vision-Language
  Models'
title_zh: FieldGuideRAG：面向VLM细粒度识别的图像锚定GraphRAG
authors:
- Jiacheng Ding
- Yanliang Qi
- Cong Guo
- Peihua Mai
affiliations:
- University of Memphis
- National University of Singapore
arxiv_id: '2610.40971'
url: https://arxiv.org/abs/2610.40971
pdf_url: https://arxiv.org/pdf/2610.40971
published: '2026-10-29'
collected: '2026-11-02'
category: RAG
direction: 多模态GraphRAG · 细粒度视觉识别
tags:
- GraphRAG
- VLM
- Fine-grained Recognition
- Multimodal RAG
- Training-free
one_liner: 提出免训练图像锚定GraphRAG，通过VLM两两比对候选参考图提升细粒度识别准确率
practical_value: '- 做电商同款/相似款细粒度召回时，可将商品主图存储在GraphRAG节点，用冻结VLM两两比对query图与候选图，避免文本描述漏损视觉特征，提升匹配准确率

  - 多模态召回排序阶段，视觉匹配分、结构化属性（如发货地、用户场景）分可采用log-linear融合，效果优于加性融合，仅需小量验证集调参

  - 多候选图比对场景不要将所有图塞入同一个prompt，VLM多图比对存在严重位置偏见，两两独立比对鲁棒性更强且可并行降时延

  - 商品属性问答场景可先识别实体再直接读取预存结构化属性，比让LLM从长上下文摘信息的准确率最高提升6个点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有VLM在细粒度识别任务（如相似物种、同款商品）上表现极差，现有多模态GraphRAG仅存储实体文本描述，无法覆盖区分相似实体的微小视觉特征；多图RAG将所有候选图塞入同一prompt，VLM多图比对能力弱且存在严重位置偏见，召回准确率低。
### 方法关键点
- 构建图像锚定知识图谱：每个实体节点存储1张实拍参考图，关联近缘实体、地理分布、结构化属性三类边，数据全部来自公开数据集无需额外标注
- 候选召回：用SigLIP生成query和节点图的嵌入，取Top8相似实体+Top1实体的近缘实体组成候选池，召回覆盖率达90%以上
- 两两验证：冻结VLM独立比对query图与每个候选的参考图，输出匹配概率，全程无需训练，不同候选的比对可并行执行
- 多源分数融合：采用log-linear公式融合VLM匹配概率、召回相似度、地理分布概率，参数通过小量验证集网格搜索确定；实体识别后直接取其属性边回答问题
### 关键结果
在CUB-200鸟类、Wikidata、4个iNaturalist物种数据集上测试，对比SigLIP召回、文本RAG、多图RAG等基线：候选验证准确率比SigLIP最高高16个点，加入地理分布边后iNaturalist数据集准确率提升7-19个点，28820条属性问答的准确率最高达89.5%，比多图RAG+属性prompt方案最高高6个点。

最值得记住的一句话：细粒度多模态匹配场景下，实体实拍图的信息增益远大于文本描述，VLM两两独立比对的效果显著优于单prompt多图比对。
