---
title: 'SIDScope: A Diagnostic Resource for Semantic-ID Interfaces in Generative Recommendation'
title_zh: SIDScope：生成式推荐语义ID接口的诊断工具集
authors:
- Jiandong Ding
- Huijie Qin
- Tiandeng Wu
- Yi Cao
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2608.18779'
url: https://arxiv.org/abs/2608.18779
pdf_url: https://arxiv.org/pdf/2608.18779
published: '2026-08-19'
collected: '2026-08-20'
category: GenRec
direction: 生成式推荐 · Semantic ID质量诊断
tags:
- Semantic-ID
- Generative-Recommendation
- Evaluation-Toolkit
- Artifact-Diagnosis
- Mapping-Lifecycle
one_liner: 开源面向生成式推荐Semantic ID接口的多维度诊断工具集，覆盖映射质量、生命周期、生成轨迹校验
practical_value: '- 上线Semantic ID架构的生成式推荐前，可复用SIDScope的D1-D5诊断项（碰撞率、前缀对齐度、头尾分辨率等）提前排查映射缺陷，避免训练完生成器才发现地址空间问题，节省研发成本

  - 做SID映射迭代/版本刷新时，用配套的校验流程检查新旧映射兼容性，不要默认老生成器可以直接复用，必须做独立的handoff校验，避免上线后无感知效果下降

  - 优化生成式推荐解码链路时，可复用论文提出的路径-物品解析校验逻辑，提前识别目标路径存活但实际召回不到唯一物品的1.2-3pp效果损耗，针对性优化映射去重规则

  - 团队内部做SID tokenizer选型对比时，可复用标准化的artifact准入协议和多维度指标，避免仅看下游NDCG等粗粒度指标，忽略底层地址空间的结构性风险'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐中Semantic ID作为item tokenizer与生成器之间的可复用接口，缺乏统一的质量诊断标准，业界普遍仅依赖下游推荐粗粒度指标评估，无法提前识别映射碰撞、前缀语义缺失、迭代兼容性等底层问题，映射刷新或跨场景复用时易出现无感知效果损耗。
### 方法关键点
- 定义标准化SID artifact准入协议C0-C5，统一映射、元数据、交互日志、生成轨迹的接入格式，支持跨不同tokenizer方案的公平对比
- 设计D1-D7多维度诊断指标，覆盖地址空间利用率、全码碰撞率、前缀行为对齐度、头尾物品分辨率、trie结构、映射刷新差异、生成路径-物品解析效果7个维度
- 支持机制条件性校验，可分别评估映射在前缀依赖的召回场景、前缀无关的打分场景下的适配性
### 关键结果
基于Amazon、Yelp共9个开源SID映射数据集验证：
1. 前缀对齐度与前缀召回场景的候选曝光率Spearman相关性达0.976，对前缀无关的生成器下游效果无稳定相关性
2. 训练完成的生成器链路中，目标路径存活但无法唯一召回目标物品的效果gap达1.2-3.0个百分点
3. 映射修复后直接复用原有生成器无法恢复效果，必须做独立的交接校验
### 核心结论
Semantic ID接口健康度是多信号组合，不能用单一的下游推荐指标代替全链路的映射质量诊断。
