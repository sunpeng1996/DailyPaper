---
title: 'OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs'
title_zh: OmniAssistBench：面向全模态大模型的助手式交互评测基准
authors:
- Xianyun Sun
- Chaoyou Fu
- Zhengye Zhang
- Feiyang Duan
- Qingyuan Cao
- Yonghui Niu
- Sihang Yuan
- Ge Zhang
- Caifeng Shan
affiliations:
- Nanjing University
- Nankai University
- University of Waterloo
arxiv_id: '2608.21360'
url: https://arxiv.org/abs/2608.21360
pdf_url: https://arxiv.org/pdf/2608.21360
published: '2026-08-20'
collected: '2026-08-24'
category: Eval
direction: 全模态大模型 · 交互式助手评测
tags:
- Omni-LLM
- Benchmark
- Video Assistant
- Multimodal Evaluation
- Interactive Understanding
one_liner: 基于互联网视频逆向工程构建多轮交互数据集，评测全模态大模型的实时视频助手能力
practical_value: '- 做交互式Agent评测时，可借鉴「固定路径先验+逆向视频编辑」方法，解决动态交互路径发散导致的评测不标准问题，无需录制大量真人交互数据，大幅降低标注成本

  - 多轮开放问答的评分可采用「标准答案语义匹配+核心关键点校验」的双维度机制，搭配不同大模型裁判的一致性校验，既避免评分僵化又保证可信度，适合测生成式推荐/Agent的回答质量

  - 开发实时多模态交互Agent（如电商直播智能助手、AR导购助手）时，重点优化三个共性短板：手势等非语音指令识别、长上下文跨轮记忆、延迟响应时机判断

  - 处理长视频输入时，无需盲目降低分辨率堆叠上下文长度，实测收益极低，优先针对性做长期记忆的抽取与存储，提升多轮交互表现的投入产出比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Omni-LLM正逐步向实时视频助手演进，但传统静态视频理解评测无法适配交互场景下模型输出动态影响用户行为、交互路径发散的问题，也未覆盖真实交互所需的手势识别、长上下文记忆、主动响应时机判断等核心能力，缺乏标准化的统一评测基准。

### 方法关键点
- 数据构建：采用「视频逆向工程」pipeline，从现有互联网视频中归纳固定交互路径先验，再按流程拆分视频、嵌入多轮用户指令（语音/手势/OCR形式），规避交互路径发散问题，总投入超1000专家工时
- 评测框架：分为两层，基础层测评基础交互感知能力（社会感知、时间感知、非语音指令跟随等），进阶层测复杂助手能力（上下文感知响应、主动响应、流程跟踪等），额外新增3个真实场景case（会议模拟、盲人辅助、手作流程跟踪）覆盖综合能力
- 评分机制：采用开放问答格式，用「语义相似度+核心关键点匹配」双维度评分，同时要求模型无需回复时输出`[KEEP QUIET]`，惩罚冗余和幻觉内容

### 关键实验结果
覆盖11款主流闭源/开源Omni-LLM，闭源模型中Gemini-3-Pro得分最高66.4/100，开源模型中Qwen3-Omni-Instruct得分最高51.2/100；当前模型普遍存在4个核心瓶颈：手势等视觉指令跟随准确率低、长上下文记忆不足、无法延迟响应到目标事件、跨轮丢失初始用户目标。

### 核心结论
当前即使是最先进的Omni-LLM，距离能在真实场景落地的可靠交互式助手还有至少30分的性能缺口，非语音指令识别、长上下文记忆、响应时机判断是最核心的优化方向。
