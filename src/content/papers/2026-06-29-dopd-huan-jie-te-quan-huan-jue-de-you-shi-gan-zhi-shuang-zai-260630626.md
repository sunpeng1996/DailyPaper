---
title: 'DOPD: Dual On-policy Distillation'
title_zh: DOPD：缓解特权幻觉的优势感知双在线策略蒸馏
authors:
- Xinlei Yu
- Gen Li
- Qingyi Si
- Guibin Zhang
- Yuqi Xu
- Congcong Wang
- Shuai Dong
- Kaiwen Tuo
- Xiangyu Zeng
- Kaituo Feng
affiliations:
- NUS
- MMLab CUHK
- PKU
- JD Explore Academy
arxiv_id: '2606.30626'
url: https://arxiv.org/abs/2606.30626
pdf_url: https://arxiv.org/pdf/2606.30626
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 大模型蒸馏 · token级自适应优化
tags:
- On-policy Distillation
- Knowledge Distillation
- LLM
- VLM
- Token Adaptation
one_liner: 提出token级动态路由蒸馏，解决特权信息引入带来的蒸馏性能退化问题
practical_value: '- 给带辅助特权信息（如检索提示、推理hint、商品结构化标注）的大模型蒸馏场景，可复用「特权优势gap」区分真实能力差和信息不对称gap，避免学生学习不可复现的shortcut

  - 可直接复用token差异化蒸馏策略：高能力差token用全词表强监督，低价值token用轻量弱正则，兼顾蒸馏增益和计算开销

  - 蒸馏引入辅助信息时，优先选择能力引导类hint（如推理步骤提示、实体位置标注）而非直接给最终答案，能最大化蒸馏增益，这个结论可直接落地'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有On-policy蒸馏（OPD）通过给教师/学生引入特权信息（如推理提示、结构化视觉标注）提升蒸馏上限，但存在未被解决的「特权幻觉」问题：教师和学生的性能gap混杂了两种完全不同的成分，可学习的真实能力差、不可复制的信息不对称gap；加上传统OPD对所有token统一强度蒸馏，会导致学生拟合特权捷径、训练熵坍缩，最终蒸馏效果远低于理论上限。

### 方法关键点
- 定义**特权优势gap**：相同特权输入下，教师和学生的token级对数概率差，用来分离真实能力差和信息不对称带来的虚假gap
- 按优势gap和教师/学生的相对预测概率，将token分成四类，动态分配不同监督源、强度、目标的蒸馏策略：
  1. 低gap高低概率：轻量Top-K KL教师蒸馏，保守吸收有用信息
  2. 低gap低低概率：弱停止梯度学生自正则，稳定训练避免噪声干扰
  3. 高gap高教师概率：全词表JS散度强教师蒸馏，充分转移核心能力
  4. 高gap高学生概率：轻量学生自蒸馏，保留有效探索空间

### 关键实验
在LLM（5组不同尺度Qwen3模型对）、VLM（Qwen3-VL 8B→2B）场景，对比了Vanilla OPD、ExOPD、Uni-OPD、SDPO等10+种SOTA baseline：DOPD比Vanilla OPD在LLM平均提升7.5个点，VLM平均提升6.0个点；对8B→0.6B大尺度 mismatch场景，Vanilla OPD仅提升3.5点，DOPD提升14.1点，恢复了53%的师生性能gap；OOD泛化比最优 baseline高3.1-4.3个点，训练过程更稳定，不会提前出现熵坍缩。

最值得记住的一句话：不是所有教师的优势都是可迁移能力，要过滤掉信息不对称带来的虚假优势再蒸馏
