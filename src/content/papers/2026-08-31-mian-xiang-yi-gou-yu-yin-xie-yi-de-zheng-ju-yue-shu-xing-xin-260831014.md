---
title: Evidence-Bounded Mental Health Reasoning from Heterogeneous Speech Protocols
title_zh: 面向异构语音协议的证据约束型心理健康推理
authors:
- Chengyuan Gao
- Jiang Wu
- Tao Lu
- Jiayan Guo
- Mingkun Xu
- Tianyi Zang
- Shangyang Li
affiliations:
- Beijing University of Posts and Telecommunications
- Harbin Institute of Technology
- Renyixun Health Technology Co., Ltd.
- GDIIST
- Tencent
arxiv_id: '2608.31014'
url: https://arxiv.org/abs/2608.31014
pdf_url: https://arxiv.org/pdf/2608.31014
published: '2026-08-31'
collected: '2026-09-02'
category: Reasoning
direction: 多模态证据约束推理 · 临床NLP
tags:
- LLM Reasoning
- Multimodal
- Hallucination Mitigation
- Clinical NLP
- Evidence Control
one_liner: 提出证据约束框架EviBound与配套基准，解决多模态心理健康筛查中LLM推理越界与幻觉问题
practical_value: '- 多源异构用户行为数据分析场景（如电商搜索/浏览/加购行为融合）可复用「profile感知规划器+边界校验器」架构，区分不同数据源置信度，避免低可信度数据引发的推荐/广告决策幻觉

  - 多模态Agent推理链路可引入5向声学共识类的跨模态证据对齐机制，降低直播、短视频等场景中单模态噪声带来的推荐偏差

  - 高风险决策类Agent（如营销归因、客诉处理）可复用证据权限标注方法，给不同数据源绑定许可边界，杜绝无依据结论输出'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前多模态心理健康筛查模型默认所有临床语音协议的证据有效性等价，强制统一推理会引发症状幻觉、过度断言问题，即使是长CoT LLM也会加剧推理边界越界。
### 方法关键点
1. 将多模态筛查任务重定义为证据约束推理问题，构建包含1870个跨6类异构源的证据包基准，标注显式模态掩码与证据权限；
2. 提出EviBound协议感知证据控制框架，通过profile感知规划器限制推理范围，基于5向声学共识调度证据工具，设置边界批评器抑制无依据声明。
### 关键结果
留存测试集抑郁识别AUROC达0.8658，比最强全模态基线高出0.0811，同时实现零声明越界。
