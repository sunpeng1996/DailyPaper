---
title: 'Beyond Downstream QA: Rethinking How We Evaluate Agent Memory'
title_zh: 《超越下游QA：重新思考智能体记忆的评估范式》
authors:
- Sebastian-Antonio Toma
- Jean de Kernier
- Mike Ply
- Oliviu Matei
affiliations:
- Amazon Web Services
- Technical University of Cluj-Napoca
arxiv_id: '2610.22209'
url: https://arxiv.org/abs/2610.22209
pdf_url: https://arxiv.org/pdf/2610.22209
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: Agent 记忆系统评估优化
tags:
- Agent Memory
- Benchmark
- Intrinsic Evaluation
- Extrinsic Evaluation
- LLM Agent
one_liner: 提出首个Agent记忆内在评估基准FEB-30，可直接校验记忆存储状态，规避下游QA评估的偏差
practical_value: '- 评估自建Agent记忆系统时，可复用FEB-30的双评估范式：先直接校验记忆存储的事实完整性、更新正确性，再测下游QA效果，避免被LLM推理补偿的假高分或检索瓶颈的假低分误导

  - 构建事实演化类评测数据集时，可复用范式反转方法：先定义ground truth事实轨迹，再生成对应文档，无需人工标注即可获得确定性基准，大幅降低评测集构建成本

  - 优化Agent记忆模块时，可参考论文的诊断拆解维度：将错误定位到提取/合成/更新/冲突四个阶段，针对性优化分类逻辑、时序校验、多源归因能力，提升记忆准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agent记忆评估仅依赖下游QA准确率，混淆了记忆存储、检索、生成三个模块的能力，存在两类严重偏差：LLM推理补偿产生的假阳性（记忆错误但回答正确）、检索瓶颈产生的假阴性（记忆正确但回答错误），无法定位故障环节，阻碍记忆系统迭代。

### 方法关键点
- 提出FEB-30基准：包含30条事实演化轨迹，覆盖6类诊断场景（LLM补偿、检索瓶颈、操作分类、事实合成、时序正确性、多作者归因）和3个难度等级，每条轨迹定义了每一步的确定性记忆ground truth
- 采用范式反转的文档生成流程：先定义事实演化轨迹，再通过多模型轮换生成、3模型校验生成对应文档，避免人工标注的主观性和高成本
- 设计双维度评估体系：内在评估直接对比记忆存储内容与ground truth，计算claim覆盖率、更新检测召回率、错误更新率等指标；外在评估沿用传统QA准确率，同时计算两类评估的平均绝对偏差（MAD）

### 关键实验结果
在主流的extract-embed-classify-synthesize架构的Agent记忆系统上测试，结果显示：① 内在与外在评估的平均偏差达16个百分点，44%的轨迹偏差超过15%，仅用QA评估会在约1/5的场景下得出错误结论；② 记忆系统对记忆操作（创建/更新/强化/替换）的分类准确率仅20%，这类故障完全无法被外在评估检测；③ 多作者归因、时序演化是记忆系统的最薄弱环节，内在准确率仅41.5%、59.3%。

最值得记住的一句话：Agent记忆的内在评估是外在评估的必要补充，二者分别对应软件工程的单元测试和端到端测试，结合使用才能同时保障系统的正确性和实用性。
