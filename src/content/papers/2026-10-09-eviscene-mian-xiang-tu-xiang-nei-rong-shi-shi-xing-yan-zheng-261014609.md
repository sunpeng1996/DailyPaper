---
title: 'EviScene: Beyond "Is It AI?" for Agentic Image Factuality Assessment'
title_zh: EviScene：面向图像内容事实性验证的多模态智能体框架
authors:
- ZiAn Wang
- Ruiqi Liu
- Zhengbo Zhang
- Yi Han
- Jialiang Shen
- Ruoxin Chen
- Manni Cui
- Ximo Zhu
- Jin Jiang
- Mingzhe Liu
affiliations:
- Jilin University
- Institute of Automation, CAS
- Tencent Youtu Lab
- University of Sydney
- Huazhong University of Science and Technology
arxiv_id: '2610.14609'
url: https://arxiv.org/abs/2610.14609
pdf_url: https://arxiv.org/pdf/2610.14609
published: '2026-10-09'
collected: '2026-10-14'
category: Agent
direction: 多模态Agent · 图像事实性核验
tags:
- Multimodal Agent
- ReAct
- Fact Verification
- Image Understanding
- Benchmark
one_liner: 提出无前置声明的图像事实性评估任务，配套10k+样本基准和多模态ReAct验证智能体
practical_value: '- 电商商品图/营销素材真伪核验场景可复用「视觉检测+检索对齐+证据校验」的ReAct多模态Agent架构，替代纯视觉判别方案，提升事实性判定准确率

  - 小模型Agent训练可复用SFT+特权自蒸馏（PSD）两阶段范式：先用大模型生成的高质量轨迹做SFT，再用自蒸馏修正错误决策，大幅缩小与大模型的能力gap

  - 多模态Agent工具选型可参考论文ablation结论：web搜索、图像检索对证据充分度的提升幅度远大于证据校验工具，优先保障检索链路能力

  - UGC/营销内容合规审核场景可复用论文12类事实错误分类体系，覆盖属性、上下文、关系三类错误，完善审核规则'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有图像真实性检测仅聚焦判断是否为AI生成，无法验证图像内容本身是否符合客观事实；传统多模态事实核验依赖前置文本声明作为锚点，无法直接对单张图片完成事实性判定，无法满足UGC内容审核、营销素材校验等场景的无前置输入核验需求。

### 方法关键点
- 构建EviLens基准：包含10174张标注图像（3114张符合事实、7060张不符合事实），覆盖12类事实错误，同时评估判定准确率和证据充分性
- 设计EviScene多模态ReAct Agent：交替执行视觉检测、外部检索（网页/图像搜索）、证据对齐三类动作，根据中间结果迭代优化核验问题，最终输出带证据链的判定结果
- 两阶段训练范式：先用大模型生成的4872条经过审核的高质量轨迹对Qwen3.5-9B做全参数SFT，再用特权自蒸馏（PSD）对智能体自身决策做修正，无需暴露正确答案即可提升小模型决策质量

### 关键结果
在1527张样本的测试集上，SFT+PSD训练的Qwen3.5-9B Agent达到79.05%的平衡准确率，严格证据充分率（SESR）52.26%，相比同基座基础Agent分别提升6.71、9.37个百分点，SESR为所有参评Agent最高；去掉网页搜索会让SESR下降16.37个百分点，去掉图像检索下降12.25个百分点。

### 核心结论
判断图像真实性不能仅靠视觉特征或生成来源，必须结合外部事实证据验证内容本身的合理性
