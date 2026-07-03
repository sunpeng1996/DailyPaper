---
title: 'HERMES: A Multi-Granularity Labeling Substrate for Pre-training Data Mixtures'
title_zh: HERMES：面向预训练数据混合的多粒度标注底层框架
authors:
- Ziyun Qiao
- Yue Min
- Ruining Chen
- Yujun Li
affiliations:
- Wizard Quant
- Peking University
- University of Science and Technology of China
arxiv_id: '2607.02266'
url: https://arxiv.org/abs/2607.02266
pdf_url: https://arxiv.org/pdf/2607.02266
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: LLM预训练 · 多粒度数据混合标注
tags:
- Data-Mixing
- Pre-training
- Residual-Vector-Quantization
- Hierarchical-Annotation
- LLM-Data-Curation
one_liner: 通过三阶残差向量量化实现一次性文档分层标注，支持预训练数据多粒度混合调优无需重聚类
practical_value: '- 做用户/内容分层聚类时，可复用3阶RVQ+前缀控粒度的设计，一次标注即可支持粗到细多维度分组，无需每次调整聚类K值重新训练，大幅降低算力成本

  - 做召回/样本池采样时，注意粒度和topK筛选的耦合关系：若子池样本量小于400左右，子池内按质量/相关性选优的增益会完全消失，不要盲目做过细粒度的子池筛选

  - 设计语义ID体系时，可参考Learned Semantic Transform的旋转+多损失约束设计，在保留语义邻接性的同时提升量化效率，适配分层ID生成需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有预训练数据混合的标注体系仅支持固定单一粒度（如来源、静态主题分类），调整聚类粒度需完全重新训练标注，算力成本高，限制了数据混合策略的调优空间。
### 方法关键点
- 先通过冻结编码器生成文档embedding，接入**Learned Semantic Transform（LST）**层做正交变换，同时约束结构保留、量化重建、正交性三类损失，在保留语义邻接性的同时适配量化需求。
- 接3阶残差向量量化（RVQ），每阶256个码本，输出三级分层编码`(c1,c2,c3)`，通过取不同长度前缀控制粒度：L1（c1，256粗粒度桶）、L12（c1+c2，约6.5万中粒度桶）、L123（c1+c2+c3，约13万细粒度桶），一次离线标注即可支持全粒度切换无需重聚类。
- 采样策略拆为两级：Stage1是L1层外权重（Uniform/DoReMi），Stage2是子桶内采样规则（最大熵覆盖/子桶内质量top30%筛选）。
### 关键实验结果
基于50M文档内部语料，训练1B参数LLM跑25B token，对比KMeans等4种256路聚类方法、WebOrganizer分类体系：1）固定DoReMi+L12粒度时，子桶内选top30%质量样本比最大熵覆盖的16任务平均准确率提升+0.0253；2）切换到L123更细粒度时，同样的top30%规则增益降至0.0002，对应子桶中位数样本量从2271收缩到429，出现候选池竞争效应；3）L1粒度下HERMES和KMeans下游效果仅差0.0002，聚类性能持平。
### 核心结论
数据混合的粒度和子桶采样规则是联合决定的，并非越细粒度越好，需匹配子池样本量保证筛选信号的稳定性。
