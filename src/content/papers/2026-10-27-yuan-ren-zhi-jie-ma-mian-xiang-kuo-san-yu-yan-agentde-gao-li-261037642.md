---
title: 'Metacognitive Decoding: Efficient Inference for Diffusion Language Agents'
title_zh: 元认知解码：面向扩散语言Agent的高效推理方法
authors:
- Mingyu Zhao
- Shuhang Lin
- Ligong Han
- Xiaojing Yu
- Zhenting Wang
- Yifei Pang
- Yang Zhou
- Dimitris N. Metaxas
affiliations:
- Rutgers University
- University of North Carolina at Chapel Hill
- Amazon
arxiv_id: '2610.37642'
url: https://arxiv.org/abs/2610.37642
pdf_url: https://arxiv.org/pdf/2610.37642
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: 扩散语言Agent · 推理加速
tags:
- Diffusion LLM
- Language Agent
- Inference Optimization
- Decoding Strategy
- Metacognitive Control
one_liner: 提出轻量元认知控制器优化扩散语言Agent解码，平均降20.6%推理FLOPs且精度持平
practical_value: '- 电商搜索/导购Agent若采用Diffusion LLM做生成，可直接复用元认知控制器架构，无需重训backbone，仅增加2层Transformer做解码控制，落地性价比极高

  - 工具调用类Agent（如电商客服、选品Agent）可复用confidence alignment策略，针对API调用、固定回答模板等高频结构预定义候选集，批量确认高置信结构token，减少冗余计算

  - 多轮交互Agent可复用flux decoding思路，动态调整每轮生成的有效窗口，避免生成超过交互边界的无效内容（如工具调用后的冗余文本），实测最高可降43%推理成本

  - 训练侧可借鉴轨迹级奖励设计，平衡任务准确率和推理成本，用GRPO训练轻量控制模块，无需修改大模型权重，业务适配成本低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
扩散语言模型（Diffusion LLM）支持并行生成，是语言Agent的优质底座，但现有固定块解码策略与Agent动态交互特性严重不匹配：一是所有token统一处理，浪费算力在高置信模板类内容上；二是固定块大小会生成超过交互边界（如工具调用触发点）的无效内容，算力冗余极高，亟需适配Agent交互场景的动态解码方案。

### 方法关键点
- 设计轻量可插拔元认知控制器，冻结Diffusion LLM backbone，仅额外增加2层Transformer，同时监控模型内部置信度、结构状态和外部Agent交互状态
- 两级级联解码策略：① 置信对齐解码：预定义高频结构（如工具调用模板、思考标签）候选集，高匹配度结构批量确认，单个token根据置信度动态调整接受阈值；② Flux解码：动态调整当前生成块的有效计算范围，屏蔽超过交互边界的位置，生成不足时可动态扩展
- 采用GRPO做轨迹级强化学习训练控制器，奖励函数同时对齐任务准确率和推理成本，平衡效果和效率

### 关键实验
在5个基准（BFCL工具调用、HotpotQA/2Wiki/MuSiQue多跳QA）测试，对比Fast-dLLM、LLaDA-8B、DLLM-Searcher等主流基线：平均比最优基线降低20.6%推理FLOPs，最高降幅达43.1%；精度最高比基线提升20.96个百分点，仅1个任务精度微降0.4个百分点可忽略；适配LLaDA、Dream等多种Diffusion LLM backbone均有效，单模块消融显示两个解码策略分别贡献16.3%、24.5%的FLOPs下降。

### 核心结论
针对Agent交互场景的计算资源调度优化，不需要修改大模型本身，仅通过轻量外挂控制器适配动态生成需求，就能实现成本大幅下降且精度不损甚至提升。
