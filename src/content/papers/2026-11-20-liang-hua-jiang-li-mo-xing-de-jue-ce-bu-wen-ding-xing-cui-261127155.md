---
title: 'The Vulnerability Window: Decision Instability in Quantized Reward Models'
title_zh: 量化奖励模型的决策不稳定性：脆弱窗口效应
authors:
- Omkar Shewale
- Deepak Kumar
- Divakar Kumar Yadav
affiliations:
- Illinois Institute of Technology
- University of Wisconsin–Milwaukee
arxiv_id: '2611.27155'
url: https://arxiv.org/abs/2611.27155
pdf_url: https://arxiv.org/pdf/2611.27155
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 大模型量化 · 奖励模型决策稳定性
tags:
- Reward Model
- Quantization
- RLHF
- Decision Stability
- 4-bit Quantization
one_liner: 揭示量化奖励模型基准准确率无法感知的决策翻转现象，刻画低边际脆弱窗口特性
practical_value: '- 量化大模型（包括推荐排序打分模型、Agent奖励评判模型）上线前不能仅看基准准确率，必须额外评估决策翻转率，重点检测得分差小的低置信度样本，避免线上行为与基准预期偏离

  - 小参数打分/奖励模型优先选择NF4量化，规避INT4-RTN带来的对抗攻击风险（如黑产构造的诱导性商品/内容更易被小模型误判为优质）

  - 多候选打分场景（如best-of-N生成推荐文案、多召回源排序）可采用级联架构：先用4bit量化小模型初筛，仅对得分差小于2倍量化噪声的top-k候选调用全精度模型重排，可节省50%左右算力同时恢复80%以上精度损失'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前奖励模型、LLM评判器普遍采用4bit量化降本，业界通常仅验证量化前后基准准确率变化极小就上线，但这种验证方式存在严重盲区，无法感知量化导致的决策偏好翻转，可能影响RLHF训练、best-of-N采样、内容过滤等下游链路效果。

### 方法关键点
- 覆盖2个系列共8个（0.6B~8B）奖励模型、3个生成式评判器、4种4bit量化方案（NF4/FP4/INT4-RTN/GPTQ），以BF16全精度结果为ground truth，定义得分差小于2倍量化噪声σ的区间为脆弱窗口
- 建模量化为得分差上的加性高斯噪声，给出翻转概率近似公式Φ(-|m|/σ)，验证其对标量奖励模型是保守上界
- 从对抗样本鲁棒性、best-of-N下游选择两个维度评估量化翻转的实际业务影响

### 关键结果
实验基于RewardBench、1260道带对抗错误候选的数学题、1000道best-of-64采样的数学题开展：量化带来的两两偏好决策翻转率达1.1%~12.3%，但基准准确率波动最低仅0.03个百分点（p=1.00）；89%~100%的翻转都发生在脆弱窗口内；0.6B小模型脆弱窗口占比达25%，8B大模型仅7%；best-of-64场景下14.6%~65.7%的最优候选选择会因量化改变，但最终答案变化仅2.6%~9.6%，选择变化是答案变化的5~8倍。

**最值得记住的一句话**：量化带来的决策变化不能用基准准确率衡量，低得分差的脆弱窗口是所有量化错误的集中发生区。
