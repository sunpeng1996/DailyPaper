---
title: 'CForce: Boosting Parallel Decoding for dLLMs via Consistency Forcing'
title_zh: 《CForce：基于一致性强制的扩散大语言模型并行解码加速方法》
authors:
- Yuji Ren
- Chenkai Xu
- Zhuocheng Gong
- Jianguo Li
- Zhijie Deng
affiliations:
- Shanghai Jiao Tong University
- Ant Group
arxiv_id: '2608.13925'
url: https://arxiv.org/abs/2608.13925
pdf_url: https://arxiv.org/pdf/2608.13925
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 扩散大模型 · 并行解码优化
tags:
- dLLM
- Parallel Decoding
- Consistency Distillation
- Knowledge Distillation
- Diffusion Model
one_liner: 通过自生成轨迹的相邻阶段对齐蒸馏，在不损失质量前提下提升dLLM并行解码效率
practical_value: '- 生成式推荐/电商文案生成场景若采用dLLM，可直接复用CForce的自轨迹蒸馏流程，无需额外教师模型即可提升并行解码速度20%+，同时不损失生成质量，降低推理成本

  - Confidence Adaptive KL Divergence（CAD）可迁移到所有生成式模型蒸馏任务，基于教师输出置信度动态切换正向/反向KL，避免反向KL的模式崩塌问题，同时保留正向KL的稳定性

  - 自轨迹阶段对齐的思路可复用在推荐系统的排序/召回模型蒸馏中，利用模型自身的推理路径构造监督信号，降低对大参数量教师模型的依赖

  - 若业务中使用支持编辑的dLLM做实时Query推荐/文案生成，可扩展CForce的监督范围到后期编辑修正的Token，进一步提升高并行度下的生成准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
扩散大语言模型（dLLM）可通过单次前向预测多个Mask Token实现高并行生成，比自回归模型解码速度潜力更高，但现有dLLM在激进并行策略下，早期去噪阶段预测不可靠，误差会向后续阶段传播，严重限制速度质量权衡；且现有蒸馏方法依赖外部教师生成的轨迹，与学生模型实际推理的状态分布不匹配，训练推理对齐度差，尤其支持编辑的dLLM的后期Token修正信号没有被有效利用，亟需适配dLLM解码特性的轻量加速方案。

### 方法关键点
- 轨迹构造：用预训练dLLM自生成置信度解码轨迹，按累计新揭示Token数划分阶段，避免逐步监督的低效问题，完全匹配实际推理的Mask、揭示、编辑模式
- 一致性蒸馏目标：采用同模型Stop-Gradient的后期阶段预测作为监督，无需额外冻结教师模型；用Confidence Adaptive KL Divergence（CAD）对齐仍处于Mask的位置，基于后期预测置信度动态插值正向/反向KL，平衡分布漂移控制和模式收敛效率；用CE损失锚定新揭示的Token位置，稳定Token提交过程
- 编辑型dLLM适配：扩展CAD的对齐范围到编辑修改的Token位置，利用后期Token到Token的修正信号监督早期Mask预测
- 课程学习：训练过程逐步增大相邻阶段的上下文Gap，从易到难学习一致性约束，稳定训练

### 关键结果
在GSM8K、MATH500、MBPP、HumanEval四个基准测试，对比LLaDA2.0/2.1基线：编辑型LLaDA2.1上平均Tokens Per Forward（TPF）从6.94提升到9.08，平均准确率从85.57提升到86.41，实际吞吐量提升22.84%；非编辑型LLaDA2.0上平均TPF从3.60提升到6.42，固定TPF=8的激进解码下平均准确率比基线高18.3%。

> 最值得记住的一句话：对于迭代式生成模型，利用自身推理轨迹的后期信号监督早期预测，是无需额外教师即可提升速度质量权衡的低成本有效方案。
