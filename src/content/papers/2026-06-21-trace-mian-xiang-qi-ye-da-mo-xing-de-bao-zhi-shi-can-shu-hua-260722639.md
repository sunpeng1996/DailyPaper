---
title: 'TRACE: Business Rule-Grounded Reasoning Curriculum for Knowledge-Preserving
  Parametric Tool Retrieval in Enterprise LLMs'
title_zh: TRACE：面向企业大模型的保知识参数化工具检索训练框架
authors:
- Sai Shruthi Sistla
- Ashutosh Hathidara
- Christopher Toukmaji
- Mayank Shrivastava
- Karthikeyan Asokkumar
affiliations:
- SAP Labs
arxiv_id: '2607.22639'
url: https://arxiv.org/abs/2607.22639
pdf_url: https://arxiv.org/pdf/2607.22639
published: '2026-06-21'
collected: '2026-07-29'
category: Agent
direction: Agent工具调用 · 参数化工具检索优化
tags:
- Tool Retrieval
- LoRA
- SFT
- Chain-of-Thought
- Parametric Retrieval
- Enterprise LLM
one_liner: 提出双阶段训练课程结合业务规则推理增强，实现保知识低延迟的企业级参数化工具检索
practical_value: '- 做Agent工具检索/API路由系统时，可复用两阶段LoRA训练范式：第一阶段做多格式工具知识记忆，从根源缓解后续检索训练的灾难性遗忘，效果优于直接做检索任务微调

  - 面临语义高度重叠的候选召回场景（如电商相似商品/相似权益/相似入口），可引入领域规则增强的CoT训练数据，针对易混淆case分明确、隐含、异常三种query风格生成样本，能显著提升难例召回

  - 生成式检索推理可替换约束波束搜索为单贪婪解码，在达到可比召回的前提下，延迟降低10倍、吞吐量提升200倍，完全适配高并发生产场景要求

  - 多阶段微调时可复用MCQ/QA探针体系，每个阶段监控领域知识遗忘程度，快速定位任务性能和知识保留的帕累托最优平衡点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有参数化工具检索方案存在两大核心缺陷：一是训练时会灾难性遗忘已学到的工具知识，二是依赖约束波束搜索解码延迟高，无法满足企业级生产并发要求；同时嵌入检索对语义重叠的工具召回率极低，81.7%的错误源于无法识别业务规则（如API弃用、版本约束），这类规则无法从工具描述中推断，无法通过优化嵌入模型解决，亟需兼顾知识保留、高召回、低延迟的工具检索方案。
### 方法关键点
- 两阶段训练课程：Stage1复用ToolSense的多格式记忆SFT，用LoRA训练工具描述到虚拟token的正向、反向映射及多选判别任务，完成工具知识的参数化内化
- Stage2核心是推理增强检索SFT，训练模型先输出思考trace再输出工具token列表，数据分为两支：一是RRB跨难度分层生成的通用query-tool对，二是基于领域专家整理的业务规则生成的易混淆case query，覆盖明确、隐含、异常三种规则触发场景
- 训练时将trace里的工具名替换为对应的虚拟token，强化工具语义和token的绑定，避免知识遗忘；推理时用单贪婪解码，无需约束波束搜索或前缀树匹配
### 关键结果
基于8283个跨HR、财务两个领域的企业工具数据集评测：
- 知识保留：对比非推理基线，MCQ准确率提升28pp，QA准确率提升9pp，无明显知识遗忘
- 召回率：Domain A（HR）R@gen达86%，Domain B（财务）达60%，远超嵌入基线的27%、52%
- 性能：单用户请求延迟1.9s，比10波束约束搜索低10倍，并发32时吞吐量达11.2qps，提升200倍
### 核心结论
生成式检索任务中，加入显式推理trace的训练目标，既能缓解灾难性遗忘，又能大幅降低推理延迟，是兼顾效果和性能的可行路径。
