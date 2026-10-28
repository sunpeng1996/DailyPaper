---
title: 'MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned
  World Model'
title_zh: MLE-World：基于学习的世界模型预测机器学习实验执行结果
authors:
- Brian Ko
- Han Wang
- Hejia Geng
- Li Erran Li
- Sherry Yang
affiliations:
- University of Washington
- University of Illinois at Urbana-Champaign
- University of Oxford
- Columbia University
- New York University
arxiv_id: '2610.37175'
url: https://arxiv.org/abs/2610.37175
pdf_url: https://arxiv.org/pdf/2610.37175
published: '2026-10-26'
collected: '2026-10-28'
category: Agent
direction: Agent 世界模型 执行结果预测优化
tags:
- World Model
- LLM Agent
- Test-Time Scaling
- Confidence Gating
- MLE Agent
one_liner: 微调4B Qwen模型作为MLE世界模型，无需执行代码即可预测输出，降低Agent实验探索成本
practical_value: '- 可复用轻量小模型SFT做领域专用世界模型的思路：针对业务高频高成本的执行环节（如推荐策略冷启动效果预判、广告创意投放效果预估），用历史<输入,输出>执行对微调小模型，替代大模型prompt或真实执行，大幅降本提效

  - 置信度门控的选择性执行机制可直接迁移：基于模型首个输出token的概率计算置信度，仅对低置信度预测走真实执行，平衡预判成本和准确率，适合业务A/B实验前置筛选、Agent多候选分支剪枝场景

  - 5种测试时缩放搜索策略可复用：Best-of-N、带探索bonus的UCB排序、多候选融合等策略，适配推荐系统多候选排序、Agent多方案筛选场景，在有限成本下提升最终效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI研究Agent每次探索新方案都需真实执行ML训练/评估任务，执行成本极高，严重限制候选方案探索量；现有剪枝、排序方案仅能减少执行次数，无法提供错误日志、训练指标等反馈支撑后续debug和方案迭代，亟需低成本的执行反馈能力。
### 方法关键点
- 模型设计：基于Qwen3.5-4B做SFT，输入为代码、环境依赖、任务数据描述、执行时长限制，输出结构化结果：异常类型、终端输出、验证指标、提交标记，同时基于首个输出token（异常类型）的概率计算置信度。
- 测试时缩放（TTS）策略：基于预测结果实现5种筛选策略：Best-of-N按预测指标选最优、序列修订基于预测反馈迭代、pairwise排序、多候选融合、UCB带探索bonus的排序，每步仅选1个候选进入后续环节。
- 置信度门控：仅对低置信度预测或新最优预测执行真实跑批，高置信度直接用预测结果迭代，进一步降低执行成本。
### 关键结果
在17个MLE-bench Lite任务上测试：
- 终端输出预测准确率77.9%，远超大模型prompt baseline的41.1%，GPU推理成本低13~1061倍；
- 5种TTS策略均优于无世界模型的Base Agent，UCB策略最高提升22.1%的平均性能；
- 置信度门控可再降30%~40%的真实执行时长，性能基本无损。

**最值得记住的结论**：用领域历史执行数据微调轻量小模型做世界模型，是平衡Agent探索效率和成本的高性价比方案，远优于大模型零样本prompt。
