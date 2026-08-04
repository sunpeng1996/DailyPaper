---
title: Grounding Agentic VLMs with Dedicated Segmentation for Fine-Grained Vehicle
  Damage Assessment
title_zh: 面向细粒度车辆损伤评估的专用分割增强代理式视觉语言模型
authors:
- Vishwajeet Shivaji Hogale
- Anjali Pai
- Nitya Ravi
affiliations:
- Northeastern University
arxiv_id: '2608.02470'
url: https://arxiv.org/abs/2608.02470
pdf_url: https://arxiv.org/pdf/2608.02470
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 多模块协作视觉评估落地
tags:
- VLM
- Segmentation
- LangGraph
- Grounding
- Hallucination Mitigation
one_liner: 提出专用分割模块+LangGraph代理流水线，大幅降低VLM细粒度视觉评估的幻觉率
practical_value: '- 复杂推理Agent任务可采用「专用感知模块负责空间/精确定位+LLM/VLM负责语义/生成」的混合架构，比单纯prompting或微调大模型成本更低、稳定性更高，可直接复用在电商商品瑕疵检测、商品属性生成等场景

  - 小目标/细粒度识别任务不要盲目用focal loss处理类不平衡，会导致小目标检测完全失效，优先选择CE+Dice损失+余弦退火学习率调度，适用于商品logo识别、细小瑕疵检测等业务

  - 多步Agent流水线用LangGraph做状态管理，配合LangFuse做全链路可观测，可快速实现节点级重试、latency监控、错误排查，适合快速落地生产级Agent应用'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
VLM作为推理代理落地视觉评估场景时空间接地能力不可靠，尤其是细粒度、视觉模糊的小目标（如车辆划痕、发丝裂纹）占像素少、梯度信号弱，易和反光、表面纹理混淆，纯VLM方案语义分类准但定位幻觉多，无法满足保险定损等高准确率要求的场景需求。

### 方法关键点
- 混合架构设计：将空间接地任务交给专用多任务分割模型TinyDamage，VLM仅负责语义推理和报告生成；分割模型采用FPN多尺度特征提取+小目标对比模块+梯度感知边界模块，损失组合为CE+4*Dice+Focal+0.1*对比损失+0.05*梯度损失+分类损失
- 7节点LangGraph Agent流水线：所有VLM生成步骤都引入分割输出（图像+结构化文本摘要）作为接地上下文，支持节点级重试，搭配LangFuse做全链路可观测
- 提出DETl细粒度检测指标：针对类不平衡下的小目标接地评估，采用宽松IoU阈值（0.1）衡量检测能力，解决mIoU被大类主导的问题

### 关键实验
在CarDD数据集（4000+图像、9000+标注实例）上验证：纯VLM语义分类准确率达87.3%，但纯图像提示下报告幻觉率78%，纯文本提示幻觉率92%，加入分割接地后幻觉率降至31%；纯focal loss会导致小损伤检测完全失效（DETl=0），FPN带来最大单增益（+2.3% mIoU），全TinyDamage框架在Mask2Former上实现+6% mIoU提升；部署后分割推理延迟仅244.6ms，VLM单节点延迟2.1s，整体成功率96%。

**最值得记住的一句话**：对细粒度视觉Agent任务，「专用感知做空间接地、大模型做语义生成」的混合架构，比单纯优化大模型prompting或微调成本更低、稳定性更高。
