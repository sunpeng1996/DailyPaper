---
title: 'Evo-Bench: Can Language Models Improve Agent Harness?'
title_zh: Evo-Bench：评测大语言模型Agent Harness自主进化能力的基准
authors:
- Lisheng Huang
- Chen Yang
- Hao Zhou
- Huatong Song
- Zongchao Chen
- Ran Le
- Yang Song
- Wayne Xin Zhao
- Tao Zhang
affiliations:
- Renmin University of China
- BOSS Zhipin
arxiv_id: '2608.09096'
url: https://arxiv.org/abs/2608.09096
pdf_url: https://arxiv.org/pdf/2608.09096
published: '2026-08-09'
collected: '2026-08-11'
category: Agent
direction: Agent 自进化能力评测基准
tags:
- Agent
- Harness_Evolution
- Benchmark
- LLM_Evaluation
- Self_Improvement
one_liner: 首个专门评测LLM自主优化Agent运行框架（Harness）能力的跨领域基准套件
practical_value: '- 可复用Harness敏感度筛选方法：业务侧迭代Agent工作流时，先筛选出对框架改进敏感的任务子集，避免被基础模型能力混淆优化效果，大幅降低迭代成本

  - Agent架构迭代可参考「固定策略模型+独立进化器」的解耦设计，把工作流优化和核心推理模型拆分，方便复用不同能力的LLM分别负责执行和架构迭代

  - 进化得到的Harness具备跨模型迁移性：业务侧可先使用成本低的小模型做迭代候选，产出优化后的工作流后迁移到业务大模型，兼顾优化成本和上线效果

  - 电商搜索/导购类Agent可优先尝试自主进化Harness：搜索类任务Harness优化增益最高达34.8分，远高于办公类任务，投入性价比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评测多聚焦静态任务执行能力，无法隔离Harness（运行框架）优化效果与基础模型能力，也难以避免任务过拟合、无法覆盖长周期迭代优化场景，而Harness进化是Agent实现自进化的核心第一步，此前缺乏专门的标准化评测基准。
### 方法关键点
- 采用Harness引导的基准构建框架：先通过辅助任务进化生成多样化Harness集合，再筛选对Harness质量高度敏感的任务，避免基础模型能力干扰评测结果
- 覆盖搜索、办公、通用Agent三大领域，拆分160个验证任务+448个不相交评测任务，采用敏感度感知的分层拆分保证跨集合泛化性
- 评测流程固定策略模型，仅让进化器LLM迭代优化Harness代码，通过多轮「诊断失败-提出改进假设-修改Harness-验证效果」的流程，最终在独立评测集上评估能力
### 关键结果
- 测试9款前沿/开源LLM，顶尖模型（GPT-5.6 Sol、Claude Opus 4.8）对比初始CodeAct基线的绝对增益分别达16.6、16.1分，接近人工编写Harness的47.5分基线
- 领域增益差异显著：搜索类任务最高增益达34.8分接近人工基线，通用任务进化结果可超越人工编写的Harness，办公类任务因需要专用流程优化难度最高
- 进化得到的Harness具备跨策略模型迁移性，在Qwen、DeepSeek、GLM等不同模型上均能稳定带来性能提升
> 核心结论：当前LLM已经具备自主优化Agent工作流的能力，在通用、搜索类场景下甚至可以超过人工设计的框架，是降本提效的高潜力方向
