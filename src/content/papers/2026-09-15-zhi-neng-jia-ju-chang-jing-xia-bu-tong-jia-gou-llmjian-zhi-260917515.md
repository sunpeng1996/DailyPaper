---
title: What Breaks Under Pruning in Smart Homes, and When? Evaluating LLM Degradation
  Across Architectures and Task Complexity
title_zh: 智能家居场景下不同架构LLM剪枝退化的细粒度评估
authors:
- Congjing Zhang
- Vashishtha Patil
- Henning Lange
- Usman Aleem
affiliations:
- Alexa Home AI, Amazon.com
- University of Washington
arxiv_id: '2609.17515'
url: https://arxiv.org/abs/2609.17515
pdf_url: https://arxiv.org/pdf/2609.17515
published: '2026-09-15'
collected: '2026-09-16'
category: Eval
direction: LLM剪枝 · 工具调用性能评估
tags:
- Pruning
- Tool Calling
- MoE
- Model Compression
- LLM Evaluation
one_liner: 系统评估跨架构LLM剪枝对智能家居工具调用的影响，揭示多维度失效模式
practical_value: '- 剪枝降本优先选MoE架构：MoE剪去70%专家仅掉0.37%准确率，远优于稠密模型的断崖式下降，适合推荐/Agent等工具调用场景降本

  - 工具调用类LLM剪枝后不要只看总准确率：需单独校验实体、参数等grounded属性的准确率，这类属性会比意图类能力先退化，对应电商场景的商品ID、优惠金额、SKU识别等核心链路

  - 稠密模型剪枝比例控制在10%以内：超过10%后易出现过拒绝问题，对应电商导购/客服Agent拒绝合法用户请求，严重影响用户体验

  - 剪枝后SFT修复需针对性补充样本：重点加入部分可执行、多实体操作的样本，这类场景剪枝后退化最严重'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM是智能家居、电商导购等工具调用场景的核心底座，但部署成本高，剪枝是主流降本方案。现有研究仅评估剪枝后的总准确率，无法揭示上下文感知工具调用的具体失效模式，也不清楚不同架构、任务复杂度下的退化差异，难以指导业务落地。

### 方法关键点
- 覆盖3类主流LLM架构：稠密Transformer、稠密混合架构、MoE，适配深度、宽度、混合、专家4种剪枝方法
- 所有剪枝模型统一做SFT修复，评估维度拆为两层：动作组件（操作、设备、参数、值）、任务复杂度（简单、中等、复杂、部分可执行、不可执行）
- 总评估样本超19500条，来自3个公开/私有智能家居工具调用数据集

### 关键结果数字
- 稠密模型剪枝安全区间极窄：10%以内剪枝准确率下降<0.6%，超过后出现断崖式退化；MoE剪去70%专家仅下降0.37%准确率，鲁棒性极强
- 剪枝先退化grounded特异性：50%剪枝比例下，设备、值预测准确率分别比操作、参数预测多下降3.1%、6.2%
- 部分可执行请求剪枝敏感度最高：每多10%剪枝比例，准确率下降10.3%，远高于简单请求的7.7%
- 稠密模型50%剪枝后，合法请求的错误拒绝率最高达80.8%，仅不可执行请求的拒绝准确率保持较高水平

### 最值得记住的一句话
工具调用类LLM剪枝不能只看总准确率，必须针对业务核心组件（实体、参数）、高敏感场景做细粒度评估，MoE是剪枝降本的首选架构
