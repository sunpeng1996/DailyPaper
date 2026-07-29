---
title: 'Pass the Baton: Trajectory-Relayed On-Policy Distillation'
title_zh: 轨迹中继式在策略蒸馏：解决大模型在策略蒸馏的前缀失效问题
authors:
- Haolei Xu
- Xiaowen Xu
- Haiwen Hong
- Zixuan Ni
- Hongxing Li
- Yiwen Qiu
- Weiming Lu
- Yongliang Shen
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2607.26057'
url: https://arxiv.org/abs/2607.26057
pdf_url: https://arxiv.org/pdf/2607.26057
published: '2026-07-27'
collected: '2026-07-29'
category: Training
direction: 大模型蒸馏 · 在策略训练效率优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Reasoning
- Speculative Decoding
one_liner: 通过无标签师生推理方向分歧触发教师短序列接管，大幅提升在策略蒸馏的效果与训练效率
practical_value: '- 做电商导购Agent/生成式推荐小模型蒸馏时，可复用无标签反思词分歧触发逻辑，无需额外标注即可降低蒸馏的标注成本，同时保留小模型原生推理分布

  - 长链推理场景（如复杂用户需求理解、多轮导购对话）可借鉴该纠错思路：检测到推理偏离信号时触发大模型短序列接管纠错，在低延时开销下提升输出准确率

  - 工程实现可直接复用基于投机解码的统一师生生成调度方案，无需维护两套独立生成流水线，大幅降低蒸馏流程的调度与通信开销

  - 可参考中继预算（M、L）的设计思路，限制大模型干预的次数和长度，平衡纠错效果与业务场景对小模型原有推理风格、特性的保留要求'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
在策略蒸馏（OPD）将监督信号锚定在学生模型自身生成的轨迹上，能有效缓解训练-推理分布偏移，是大模型强到弱蒸馏的主流方案，但存在严重的前缀失效问题：学生一旦在早期推理步骤选择错误方向，后续所有生成都会基于错误偏差，产出大量无效的误导性序列，既浪费训练算力，也会引入不可靠的监督信号。现有固定截断、离线轨迹改写等解决方案，都存在无法适配实际推理失效位置、改写存在人工痕迹等缺陷。
### 方法关键点
1. **无标签接管触发**：预定义反思词集合（But、Wait、However等转折类词汇），当教师模型的top1输出为反思词、学生模型的topK输出中无反思词时，判定为前缀失效，触发教师接管，无需外部标注或奖励模型
2. **中继轨迹构造**：设置中继预算（总接管次数M、单次接管生成段落数L），教师仅生成短纠错序列后交回学生继续生成，M次接管后直接终止轨迹，保证整体轨迹接近学生原生分布
3. **高效工程实现**：基于投机解码引擎统一师生生成调度，学生作为草稿模型、教师作为目标模型，无需切换两套独立生成流水线，算力开销极低
### 关键结果
以Qwen3-4B-Instruct为教师，Qwen3-0.6B/1.7B无思考版为学生，在8个数学推理Benchmark上测试：1.7B学生平均准确率较标准OPD提升5.73%，较最强基线FastOPD提升1.49%，训练轨迹长度减少50.7%；0.6B学生对应提升3.01%、0.62%，训练长度减少63.9%。
> 最值得记住：仅需最低0.35%的教师生成token做局部纠错，就能获得远优于全序列重写、固定截断的蒸馏效果
