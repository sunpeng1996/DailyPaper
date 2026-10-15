---
title: 'Jev-ToM: Evaluating Theory of Mind in Typed Decision Models'
title_zh: Jev-ToM：面向类型化决策模型的心理理论能力评估框架
authors:
- Kawai Chung
- Chunkit Chan
- Yuxuan Liu
- Yauwai Yim
- Xi Yang
- Wenbin Hu
- Huihao Jing
- Chiu Yeung Tang
- Changxuan Fan
- Ki Sen Hung
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2610.18610'
url: https://arxiv.org/abs/2610.18610
pdf_url: https://arxiv.org/pdf/2610.18610
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent心理理论能力评测 · 类型化决策模型
tags:
- Theory-of-Mind
- Typed-Decision-Model
- Agent-Evaluation
- Jev
- LLM-Benchmark
one_liner: 构建覆盖9个ToM基准的评测框架，对比类型化决策模型与生成式LLM的心理理论能力及资源开销
practical_value: '- 电商导购/客服Agent的高频用户意图、情绪、信念判断场景，可引入Jev这类类型化决策模型替代部分LLM调用，相比GPT-4.1
  nano成本降低32.7%，响应速度提升83.9%，情绪、信念类判断准确率接近甚至超过GPT-3.5

  - Agent置信度路由不要用统一阈值，需做任务级校准：0.9置信阈值下不同ToM任务保留错误率从0%到34.9%不等，需针对用户投诉情绪判断、商品需求意图判断等具体场景单独调整阈值

  - 选项类判断任务需控制候选数量：候选从8个扩展到16个时GPT-3.5准确率下降13.9个百分点，做用户意图分类、偏好判断时尽量拆分任务，控制单步候选数量不超过8个'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
对话与协作Agent需要频繁判断交互对象的信念、意图、情绪等心理状态，当前这类判断大多依赖生成式LLM，存在调用成本高、延迟高的问题。类型化决策模型主打结构化快速决策，可直接输出候选选项概率，但缺乏系统的心理理论（ToM）能力评测，无法确认是否可替代LLM完成高频有限选项的心理状态判断任务。

### 方法关键点
- 搭建Jev-ToM评测框架，将9个公开ToM基准的11117道英文题统一映射到6类ToM能力（知识获取、信念、目标/欲望/意图、情绪、社交语用、心理状态应用），标准化输入输出格式
- 对比5款类型化决策模型（Jev-1.13、Open-Jev-2B等）和7款生成式LLM（GPT-3.5、GPT-4o mini、Llama-3.1-8B等）的准确率、置信度稳定性、候选敏感度、调用成本与响应延迟
- 设计多组干预实验，验证附带理由对决策的干扰、心理状态反馈对行为预测的增益、候选数量对输出有效性的影响

### 关键结果
- Jev-1.13的源均衡准确率达73.2%，超过GPT-3.5的71.6%，在情绪类任务上领先GPT-3.5 5.1个百分点，成本比GPT-4.1 nano低32.7%，平均响应时间仅282ms，比GPT-4.1 nano快83.9%
- 置信度过滤效果高度依赖任务：0.9置信阈值下，不同任务的保留错误率从0%到34.9%不等
- 附带错误理由会将Jev原本正确的决策准确率从96.4%拉低至25.3%，候选从8个扩展到16个时GPT-3.5准确率下降13.9个百分点

最值得记住的结论：类型化决策模型在有限选项的高频判断任务上可实现比中小规模生成式LLM更优的精度-成本-延迟tradeoff，但落地必须做任务级的置信度校准、候选设计和输出校验
