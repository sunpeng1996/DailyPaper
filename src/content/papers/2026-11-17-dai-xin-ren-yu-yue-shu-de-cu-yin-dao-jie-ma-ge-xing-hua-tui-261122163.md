---
title: Cluster-Guided Decoding with Trust-Region Constraints for Personalized Recommendation
title_zh: 带信任域约束的簇引导解码个性化推荐框架
authors:
- Gezheng Wen
- Chao Shen
- Raviteja Anantha
- Tan Shen Cliff Chung
- Layne C. Price
affiliations:
- Amazon
arxiv_id: '2611.22163'
url: https://arxiv.org/abs/2611.22163
pdf_url: https://arxiv.org/pdf/2611.22163
published: '2026-11-17'
collected: '2026-11-18'
category: GenRec
direction: 生成式推荐 · 簇引导解码
tags:
- Cluster-guided Decoding
- Trust-Region Constraint
- Semantic ID
- Sequential Recommendation
- Cold-start
one_liner: 提出CG2R簇引导生成重建框架，将语义簇先验直接融入打分规则，兼顾推荐精度与低延迟
practical_value: '- 可以复用「语义簇先验直接加在item打分规则」的设计，替代传统仅用簇做召回候选池过滤的方案，兼顾语义可控性和排序精度

  - 冷启动用户无历史时可直接fallback到全局簇亲和度分布，无需额外开发冷启专属模型，适合新用户流量大的电商场景

  - 毫秒级延迟的特性适配第一阶段召回需求，稀疏大品类目录场景下收益更明显，可直接替换现有召回层粗筛逻辑

  - 可学习的簇引导权重γ无需人工调参，训练端到端自动收敛，降低业务上线调优成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐方法要么独立对每个item打分，缺乏对推荐结果所属语义域的显式控制；要么LLM类方案推理延迟过高，无法适配大目录在线召回场景；传统簇类方法仅用于候选池预筛选，无法影响最终排序逻辑，在稀疏大目录、冷启动场景下效果短板明显。
### 方法关键点
- 三阶段CG2R框架：1）簇学习阶段用RQ-VAE对item语义embedding做残差量化，生成层级语义簇和融合Semantic ID的item表示，预计算每个簇的归一化质心；2）上下文扩展阶段用因果Transformer编码用户交互历史预测下一个item表示，计算用户对各簇的亲和度，结合用户历史交互的簇分布加权融合，冷启动无历史时直接用预测的簇亲和度；3）约束解码阶段将簇先验作为信任域，以加权对数项形式直接加在item语义相关性打分上，引导排序向用户偏好的语义簇倾斜，簇引导权重γ为可学习参数，端到端优化。
- 训练目标包含下一个item预测损失和KL散度信任域惩罚项，推理时直接用融合后打分排序。
### 关键实验
在MovieLens-20M、Steam、Google Local WA三个跨领域数据集上对比MF、PMF、NeuMF、LLMRec等基线，Recall@10相对最优基线分别提升82%、37%、127%，单GPU下推理延迟仅1.6~2.5ms，远低于LLMRec的53+s延迟，稀疏大目录场景下提升幅度最大。
### 核心结论
将语义簇先验直接融入排序打分而非仅作为候选过滤条件，是兼顾推荐精度、语义可控性、低延迟的有效路径。
