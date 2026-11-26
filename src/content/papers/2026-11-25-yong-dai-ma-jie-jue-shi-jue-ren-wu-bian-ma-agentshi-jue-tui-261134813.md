---
title: 'Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video
  Models'
title_zh: 用代码解决视觉任务：编码Agent视觉推理能力优于视频生成模型
authors:
- Dezhi Luo
- Fengyuan Yu
- Haotian Zhang
- Zehong Zhao
- Ran Ji
- Siyuan An
- Huayi Qin
- Qingying Gao
- Zhongang Cai
- Lei Yang
affiliations:
- University College London
- Nanyang Technological University
- University of Southern California
- University of California, San Diego
- Carnegie Mellon University
arxiv_id: '2611.34813'
url: https://arxiv.org/abs/2611.34813
pdf_url: https://arxiv.org/pdf/2611.34813
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 视觉推理路径对比优化
tags:
- CodingAgent
- VisualReasoning
- VideoGeneration
- ProgramSynthesis
- Benchmark
one_liner: 在统一评估框架下证明编码Agent的视觉推理性能大幅领先当前最优视频生成模型
practical_value: '- 针对电商商品规格校验、营销素材合规检查等规则明确的结构化视觉任务，可优先采用「编码Agent写代码渲染+规则评估」方案，准确率比纯生成式视频模型高20%以上，落地性更强

  - 业务中可按需选择Agent的两种推理模式：通用可迁移的depictive模式适配同类型批量任务（如批量商品主图动效生成），单实例专属的propositional模式适配定制化需求（如大促专属素材生成），平衡效果与成本

  - 开放权重编码Agent的核心瓶颈是工具调用成功率，业务侧可优先做工具调用能力的定向微调，只要能稳定输出可执行代码，效果就能超过大部分非RL训练的生成式视频模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前行业普遍将视频生成模型作为视觉推理的主流方案，认为直接生成像素的「原生视觉推理」路径更可靠，但该假设从未在输入、输出、评估完全统一的框架下与符号化方案做公平对比，需验证哪种路径的推理效率与准确率更优。

### 方法关键点
- 评估框架完全对齐VBVR-Pro-Bench，编码Agent与视频模型输入完全一致（首帧+自然语言prompt），输出格式、官方规则评估器完全统一，Agent无额外特权
- 编码Agent仅可使用标准Python图像库，禁止调用生成式图像/视频模型，在CPU沙箱中运行，单实例最长执行30分钟，仅一次尝试机会
- 将Agent生成的代码分为两类：depictive程序（通用逻辑，可迁移到同任务族其他实例）、propositional程序（硬编码结果，仅适配当前单实例）

### 关键结果
在覆盖感知、抽象、空间、转换、知识5大类共500个实例的VBVR-Pro-Bench上测试：3款闭源编码Agent（Codex、Claude Code、Gemini CLI）得分分别为0.923、0.894、0.893，比最优RL训练的视频模型（得分0.670）高至少0.22；最优开源编码Agent GLM-5得分0.572，超过除RL训练版本外的所有视频模型。

**最值得记住的结论**：对于输入确定、解可计算的结构化视觉推理任务，明确的程序合成路径当前远优于隐式的视频生成路径，视觉推理不需要局限于仅操作视觉信息的系统。
