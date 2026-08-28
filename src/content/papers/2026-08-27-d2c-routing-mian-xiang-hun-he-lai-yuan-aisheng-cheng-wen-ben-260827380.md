---
title: 'D2C-Routing: Dimension-to-Composition Evidence Routing for Mixed-Origin AI-Generated
  Text Detection'
title_zh: D2C-Routing：面向混合来源AI生成文本检测的维度到组合证据路由
authors:
- Xin Chen
- Fuwei Zhang
- Yiqi Tong
- Wei Guo
- Yutian Xiao
- Fuzhen Zhuang
affiliations:
- Institute of Artificial Intelligence, Beihang University
arxiv_id: '2608.27380'
url: https://arxiv.org/abs/2608.27380
pdf_url: https://arxiv.org/pdf/2608.27380
published: '2026-08-27'
collected: '2026-08-28'
category: LLM
direction: 大模型混合来源生成文本检测
tags:
- LLM Detection
- Evidence Routing
- Text Attribution
- Content Audit
one_liner: 提出内容/表达双维度证据路由的混合AI文本检测方法，性能超基线6.5个点
practical_value: '- 电商UGC/AI混写内容审核场景可复用内容/表达双维度归因思路，替代单一AI相似度打分，区分AI生成内容、AI润色表达两类场景适配不同审核规则

  - 多维度证据路由+门控融合架构可迁移到推荐多信号融合任务，用户行为/内容属性/上下文信号分别过专属头再动态加权，提升排序/分类精度

  - 低FPR约束下的高TPR优化方法可复用在电商内容风控、广告合规审核等对误判容忍度极低的业务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI生成文本检测多为文档级二分类，无法适配人+AI协作创作的混合来源文本场景，单一AI相似度分数不能区分内容来源和表达来源差异，无法满足细分归因需求。
### 方法关键点
1. 将混合来源检测建模为维度到组合的来源归因任务，拆分内容来源、表达来源两个独立维度，交叉得到HH/HA/AH/AA四类协作类型标签
2. 提出D2C-Routing架构，将内容侧、表达侧证据分别路由到对应有监督维度头提取特征，再通过可学习门控组合层预测最终分类结果
### 关键结果
在HART基准衍生的MixD2C数据集上，四分类Avg TPR@1%FPR达到0.8603，比同拆分下的RACE-local基线高6.5个百分点；消融实验验证了路由设计有效性，其中AI内容+人类表达和全AI生成文本的区分是最难的任务边界。
