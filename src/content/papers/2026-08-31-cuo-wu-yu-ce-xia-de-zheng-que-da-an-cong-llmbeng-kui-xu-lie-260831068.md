---
title: 'Wrong Prediction, Right Answer: Recovering Evidence from Collapsed LLM Sequence
  Scores'
title_zh: 错误预测下的正确答案：从LLM崩溃序列评分中恢复证据
authors:
- Qiyao Yan
- Chenpeng Wang
- Liangming Pan
affiliations:
- Peking University
- Beijing Academy of Artificial Intelligence
- YiXin-AILab
arxiv_id: '2608.31068'
url: https://arxiv.org/abs/2608.31068
pdf_url: https://arxiv.org/pdf/2608.31068
published: '2026-08-31'
collected: '2026-09-01'
category: LLM
direction: LLM推理诊断 · 输出校准
tags:
- LLM Calibration
- Reasoning Diagnosis
- Output Bias
- Sequence Scoring
- Model Probing
one_liner: 用仅2个参数的无标签校正从LLM崩溃的输出评分中恢复隐藏的正确推理逻辑
practical_value: '- 做LLM驱动的商品分类、评论情感判别、Agent意图识别时，若发现输出集中在「中性」「无法判断」等高频标签，不要直接判定模型能力不足，可尝试加性偏移校正，仅需25个左右无标签样本就能提升准确率，成本极低

  - 在LLM-as-Judge的电商评价、广告素材打分场景下，可加入全局标签偏移校正环节，无需微调模型即可缓解输出层结构偏见，避免全局校准仅拉平分布不解决单case准确率的问题

  - 搭建电商/广告Agent时，不要仅用最终输出准确率评估模型推理能力，可结合隐藏层探针和输出评分校正，更准确判定模型真实能力边界，避免误判浪费优化资源'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM评估默认输出错误等价于推理能力不足，但大量错误本质是输出层结构偏见（如偏好高频标签、prompt表述干扰）导致的表达故障，而非内部无正确推理逻辑。此前的隐藏层探针只能证明内部存在相关信息，无法验证原生生成路径是否用到这些信息；普通输出校准仅能拉平全局标签分布，无法确认单样本推理逻辑是否被保留。

### 方法关键点
- 三阶段诊断pipeline：先通过隐藏层探针验证内部是否编码正确答案，再定位输出层评分瓶颈，最后用仅2个参数的无标签加性偏移校正（固定1个标签偏移为0，仅优化另外2个，拟合目标是让输出分布匹配标签先验，无需标注样本）
- 严格验证体系：通过TF-IDF过滤表层词匹配可解样本，用标签计数置换基线排除仅匹配全局分布的假增益，用极小样本拟合排除重学任务映射的可能

### 关键结果
在控制逻辑推理、ProofWriter、ANLI、FOLIO四类任务测试：Qwen3.5系列模型原生序列评分准确率坍缩至随机水平（0.333），仅用25个无标签样本校正即可恢复9~34个准确率百分点，效果可迁移至OLMo-2-1B、Llama-3.1-8B；校正后在TF-IDF难例上准确率仍达0.62~0.65，比标签置换基线高28~30个百分点，证明恢复了真实单样本推理逻辑而非表层匹配。

### 核心结论
LLM输出错误不代表缺乏推理能力，极有可能是输出层偏见掩盖了内部正确逻辑，极小样本无标签校正即可低成本挖掘隐藏的正确信号
