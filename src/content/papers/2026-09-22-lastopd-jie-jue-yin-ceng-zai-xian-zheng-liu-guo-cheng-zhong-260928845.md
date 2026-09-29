---
title: 'LastOPD: Taming Collapse in Latent On-Policy Distillation'
title_zh: LastOPD：解决隐层在线蒸馏过程中的性能崩塌问题
authors:
- Jie Yang
- Zhengyu Fang
- Zelin Xu
- Jiarui Sun
- Xiran Fan
- Junpeng Wang
- Liang Wang
- Qinghua Liu
- Yiwei Cai
- Yan Zheng
affiliations:
- University of Illinois at Chicago
- Case Western Reserve University
- University of Florida
- Visa Research
- The Ohio State University
arxiv_id: '2609.28845'
url: https://arxiv.org/abs/2609.28845
pdf_url: https://arxiv.org/pdf/2609.28845
published: '2026-09-22'
collected: '2026-09-29'
category: Training
direction: 大模型知识蒸馏 · 在线蒸馏性能优化
tags:
- Knowledge Distillation
- On-Policy Distillation
- Latent Alignment
- Model Compression
- LLM Training
one_liner: 仅在最后一层施加10步过渡隐层监督的在线蒸馏方案，解决隐层监督后期性能崩塌问题
practical_value: '- 做大模型到小模型的能力蒸馏时，不要盲目对齐所有中间层的隐层状态，优先对齐LM头前的最后一层通用输出，可避免跨架构蒸馏的性能崩塌，适配电商/推荐场景下大模型蒸馏到端侧/线上小模型的需求

  - 多损失联合训练时可复用10步线性过渡的权重调度策略：前期用隐层对齐快速获得性能增益，后期平滑切换到token级损失稳定效果，比硬切换效果提升8个点以上

  - 隐层相似度等中间对齐指标不能直接作为下游效果的代理指标，即使对齐度持续提升，业务效果也可能下降，必须结合业务核心指标做early stop'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有隐层在线蒸馏（OPRD）存在两个核心缺陷：一是训练前期效果快速提升，后期性能断崖式崩塌，甚至低于模型初始水平；二是隐层对齐度指标持续优化，但下游任务效果持续下降。根因是不同尺寸/架构的模型同深度层功能不匹配，强行对齐会让学生模型学习无法理解的教师状态，此前的层重映射、大激活维度掩码等方案都无法解决崩塌问题。
### 方法关键点
- 仅对齐教师与学生LM头前的最后一层隐层状态，该层是两类模型预测下一词的通用接口，无需中间层配对，仅用小型可训练MLP适配不同隐层维度
- 采用10步线性交叉过渡的损失调度：前10步隐层对齐损失权重从1线性降至0，token级OPD损失权重从0线性升至1，之后仅保留token级损失训练，避免长期隐层监督的负向作用
- 推理阶段直接丢弃适配MLP，无任何额外推理开销
### 关键实验结果
在3组跨/同架构Qwen3蒸馏任务上验证，对比纯token级OPD、全层隐层对齐OPRD等baseline：
- Qwen3-4B教师蒸馏到1.7B学生：MATH-500准确率较纯token OPD高5.55个点，8个下游数学数据集平均提升3.93个点，达到纯token OPD最终效果的训练步数减少50%
- Qwen3-8B教师蒸馏到1.7B学生：MATH-500准确率较纯token OPD高4.02个点，8个数据集平均提升2.10个点
- 同架构蒸馏场景下，性能较最优方案仅下降0.58个点，泛用性极强

**最值得记住的结论**：跨架构隐层蒸馏的增益是短期的，只有将隐层监督限制在通用接口层并及时切换到输出层监督，才能保留增益同时避免性能崩塌。
