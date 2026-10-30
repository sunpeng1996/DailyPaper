---
title: 'UGR: Unified Generative Ranking for Heterogeneous E-commerce Recommendation'
title_zh: UGR：面向异构电商推荐的统一生成式排序框架
authors:
- Zonghe Shao
- Huabin Chen
- Sitong Lu
- Fangmei Zhu
- Yingcai Ma
- Ge Fan
- Jinguo Gao
- Wei Shi
- Yanfang Liu
- Huiping Chu
affiliations:
- Alibaba Group
arxiv_id: '2610.39426'
url: https://arxiv.org/abs/2610.39426
pdf_url: https://arxiv.org/pdf/2610.39426
published: '2026-10-29'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · 跨业务异构排序
tags:
- Generative Ranking
- E-commerce Recommendation
- Multi-business Recommendation
- Permutation Preference Optimization
- Ad Debiasing
one_liner: 针对电商跨业务异构候选集设计统一生成式排序框架，兼容GSP规则平衡用户与商业价值
practical_value: '- 跨业务混排场景可直接复用统一生成式排序架构，替代分业务生成后mixrank的流程，消除位置偏移带来的效果损失

  - 训练阶段新增广告去偏塔分离历史曝光偏差，推理阶段直接加当前eCPM的设计，无需修改现有GSP定价规则即可上线，降低业务改造成本

  - 反馈监督可结合WSFT（按点击/转化加权SFT）和PermPO（基于DCG的排列偏好优化），在不降低曝光拟合度的前提下提升后端转化效果

  - 低秩候选注意力可实现千级候选的上下文建模，推理延迟仅增加12ms，满足工业级实时推荐的性能要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式排序大多基于单业务截断候选集训练，生成后需跨业务混排导致位置和上下文偏移，效果存在损失；同时仅拟合历史曝光序列无法充分利用后验点击/转化反馈，且广告历史曝光偏差会污染推荐分准确性，还要兼容现有GSP拍卖规则不能改动定价逻辑，工业落地存在多重阻碍。
### 方法关键点
- 架构层：对全请求级千级异构候选（自然品、广告、其他业务品）做统一编码，用低秩候选注意力建模跨候选交互，通过候选感知自回归解码生成排序序列
- 训练层：联合优化NTP（曝光序列拟合）、WSFT（按点击/转化反馈加权的SFT）、PermPO（基于反馈DCG构造排列偏好对做对比优化）三类目标，超越单纯曝光序列模仿
- 兼容层：训练阶段新增仅训练用的广告去偏塔建模历史eCPM带来的曝光偏差，推理阶段移除塔直接将当前eCPM与推荐分相加，完全兼容现有GSP分配和定价规则
- 推理层：用多值序列检索生成Top-N候选列表，接入现有下游评估器选最终曝光序列，最小化业务改造量
### 关键实验
基于淘宝猜你喜欢两个工业场景数据集，对比PRM、GReF等6个SOTA基线，离线IPV NDCG最高提升4.86%，CVR MAP提升2.05%；线上A/B测试相对生产基线，Core IPV提升1.76%，交易笔数提升3.29%，GMV提升2.10%，推理延迟仅增加12ms，符合线上性能要求。
### 核心结论
统一生成式跨业务排序相比分业务生成后混排，能消除上下文偏移带来的效果损失，且通过训练推理解耦的去偏设计可无缝兼容现有广告拍卖规则，落地性价比极高
