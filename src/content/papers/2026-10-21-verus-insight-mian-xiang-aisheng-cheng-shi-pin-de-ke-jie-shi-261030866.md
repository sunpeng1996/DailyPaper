---
title: 'Verus-Insight: Towards Explainable Artifact Detection in AI-Generated Videos'
title_zh: Verus-Insight：面向AI生成视频的可解释伪影检测框架
authors:
- Zhuoran Zhang
- Yang Shi
- Qixun Wang
- Tengfei Liu
- Yuqi Tang
- Xuanyu Zhu
- Yizhuo Jia
- Jingyun Hua
- Shixuan Liu
- Xianghua Ying
affiliations:
- Peking University
- Kling Team
- HKUST (GZ)
- Fudan University
- Tsinghua University
arxiv_id: '2610.30866'
url: https://arxiv.org/abs/2610.30866
pdf_url: https://arxiv.org/pdf/2610.30866
published: '2026-10-21'
collected: '2026-10-24'
category: Other
direction: AI生成视频检测 · 可解释伪影鉴别
tags:
- AIGC Detection
- Explainable AI
- Video Analysis
- Benchmark
- Artifact Detection
one_liner: 提出三阶段可解释AI生成视频伪影检测框架及配套细粒度标注评估基准
practical_value: '- 三阶段「规划-验证-聚合」结构化检测范式可迁移到电商AIGC商品素材/营销文案的错误校验场景，提升生成内容审核准确率

  - 人类锚定全流程监督+渐进式能力训练方法可复用在多步推理Agent的能力迭代中，有效降低输出幻觉

  - 细粒度人工标注基准构建方法可借鉴到生成式推荐场景的内容效果评估数据集建设流程'
score: 5
source: huggingface-daily
depth: abstract
---

### 动机
AI生成视频真实度快速提升，现有伪影检测器要么无法识别细微生成伪影，要么输出检测结果缺乏可解释的证据支撑，无法满足可信检测需求。
### 方法关键点
将伪影检测拆解为三类互补能力：Inspection Planning确定检测目标，Evidence Verification验证目标是否存在真实伪影，Evidence Aggregation整合证据输出最终判断。基于该范式训练Verus-Insight，采用人类锚定全流程监督与渐进式能力训练策略，同时发布带细粒度人工可感知伪影标注的Verus-Bench评估基准。
### 关键结果
在多基准测试中，细粒度伪影分析、AI生成视频检测性能均领先，人类感知伪影恢复能力大幅提升，无额外伪影误报增加。
