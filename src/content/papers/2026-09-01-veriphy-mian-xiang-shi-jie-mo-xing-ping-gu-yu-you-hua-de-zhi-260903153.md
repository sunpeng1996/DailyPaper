---
title: 'VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement'
title_zh: VeriPhy：面向世界模型评估与优化的智能体物理推理系统
authors:
- Wenzhuo Xu
- Yuchen Zhu
- Chongjian Ge
- Xuan Shen
- Jing Shi
- Jason Kuen
- Yongxin Chen
- Molei Tao
- Christopher McComb
- Noelia Grande Gutiérrez
affiliations:
- Carnegie Mellon University
- Georgia Institute of Technology
- Northeastern University
- Adobe Research
arxiv_id: '2609.03153'
url: https://arxiv.org/abs/2609.03153
pdf_url: https://arxiv.org/pdf/2609.03153
published: '2026-09-01'
collected: '2026-09-05'
category: Agent
direction: 智能体驱动的生成内容物理合规性评估
tags:
- Agent
- Evaluation
- Physical Reasoning
- World Model
- Auditable AI
- Video Generation
one_liner: 提出带全链路可追溯证据链的智能体物理校验框架，实现生成视频物理合规性可审计评估
practical_value: '- 电商生成商品展示视频、3D交互内容时，可复用「前置规划校验+多工具调用+证据链留存」的架构，快速检测悬浮商品、碰撞穿模等物理bug，降低劣质内容上线风险

  - 多工具调用Agent的执行逻辑可迁移到广告/推荐生成内容的合规审核场景：先静态校验执行计划合法性，再按拓扑序调用工具，全链路留存证据，出问题可快速溯源定位

  - 三值判决（支持/反对/弃权）的判定逻辑可迁移到生成式推荐的内容质量评估，证据不足时标记为弃权而非直接打回，减少优质内容的误杀率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有生成视频评估仅依赖感知质量评分或VLM二元判定，既无法定位物理规则违反的具体位置、类型，也没有可追溯的证据链，用于机器人训练、电商商品展示等对物理合理性要求高的场景时风险极高，也无法支撑生成结果的闭环迭代优化。
### 方法关键点
- 前置文本规划：未读取视频帧前就将prompt拆解为带类型的物理校验义务，生成经静态验证的执行计划，所有工具调用均提前声明，避免执行过程中随意新增逻辑
- 多工具受控执行：按拓扑序调用冻结的低阶专家工具（SAM 3分割跟踪、11类物理量测量、OCR、音频事件检测等），每个调用返回带全来源信息的证据记录，明确区分工具测量值与模型学习到的状态
- 确定性结果聚合：通过固定规则将可用证据映射为三值状态（合理/不合理/弃权），全链路证据可追溯，每个判定都能回溯到对应的prompt片段、工具调用结果与判定规则
### 关键结果
在1500条带人工标注缺陷的生成视频语料上测试，149条核心测试集共304个标注缺陷，VeriPhy可识别228个，优于开源问题分解评估器的164个，与整体prompting的222个召回率相当，但独有全链路可审计能力，可为生成系统提供可落地的反馈接口。
### 核心结论
智能体评估的核心价值不止于准确率，更在于可追溯的证据链，为生成系统的闭环优化提供明确的迭代信号。
