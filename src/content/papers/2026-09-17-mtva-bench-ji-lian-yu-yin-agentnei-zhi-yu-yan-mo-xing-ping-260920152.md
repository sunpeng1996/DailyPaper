---
title: 'MTVA-Bench: Evaluating the Language Model Inside Cascaded Voice Agents'
title_zh: MTVA-Bench：级联语音Agent内置语言模型评估基准
authors:
- Pritish Mishra
- Ishaan Kumar
- Akshat Mandoli
- Sudarshan Kamath
affiliations:
- Smallest AI
arxiv_id: '2609.20152'
url: https://arxiv.org/abs/2609.20152
pdf_url: https://arxiv.org/pdf/2609.20152
published: '2026-09-17'
collected: '2026-09-18'
category: Eval
direction: Agent评测 · 语音Agent能力评估
tags:
- Voice Agent
- LLM Evaluation
- Benchmark
- Tool Calling
- Multilingual
- Cascaded System
one_liner: 构建覆盖7语言490场景的级联语音Agent中间层LLM评测基准，分离任务与对话质量维度
practical_value: '- 电商语音外呼、智能客服类Agent的LLM选型可复用该基准的「任务完成+对话体验双维度加权」框架，避免仅看工具调用成功率忽略用户感知的体验问题

  - 级联系统中间层LLM的预上线验证可借鉴其噪声模拟设计：不需要对接真实ASR/TTS组件，即可模拟输入错误、语句拆分等生产场景，提前验证LLM鲁棒性

  - LLM-as-judge的内部评测流程可复用「强制证据引用」机制：要求法官LLM必须引用对话原文、规则原文才能给出判定，大幅降低主观偏差，提升评测可解释性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有语音Agent评测存在两类缺陷：端到端全链路评测无法分离ASR、中间LLM、TTS各模块的错误，难以定位问题根因；纯文本LLM工具调用评测忽略语音场景特有的ASR识别错误、VAD语句拆分、TTS输出格式要求等约束，无法真实反映级联语音Agent中LLM的实际表现。
### 方法关键点
- 固定评测边界为ASR与TTS之间的LLM层，模拟生产输入环境：自动注入ASR错误、VAD拆分噪声，调用侧由LLM按预设身份即兴对话，后端为Mock服务，仅当传入参数符合要求时返回正确结果
- 三层评分机制：代码侧确定性校验工具调用的名称、参数、顺序正确性；场景法官LLM基于场景规则评分，必须引用对话原文索引和规则原文才能输出判定；对话法官LLM仅访问对话流，不知道任务目标，避免锚定偏差；任务得分与对话得分各占50%权重
- 覆盖金融、零售、物流、农业等9个领域，包含49个Agent配置、490个经过审核的多轮场景，支持7种语言
### 关键实验
在7款主流LLM的对比测试中，6款模型的工具选择正确率差距仅6.4分，但整体得分差距达24.4分，差距主要来自参数正确性、调用顺序、规则合规性、工具调用前后的话术表现；最优模型gpt-5.6-sol整体得分73.9，场景通过率65%，尾部专用语音模型phonellm整体得分仅33.4，通过率3%。
### 核心结论
工具调用正确率远不能代表语音Agent的实际表现，对话体验、规则合规性、异常处理能力才是不同模型的核心差距来源。
