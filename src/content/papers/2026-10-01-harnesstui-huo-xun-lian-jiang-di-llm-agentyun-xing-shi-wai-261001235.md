---
title: 'Harness Annealing: Learning to Act with Less External Control'
title_zh: Harness退火训练：降低LLM Agent运行时外部控制依赖的方法
authors:
- Yingxuan Yang
- Huacan Chai
- Ying Wen
affiliations:
- Shanghai Jiao Tong University
- University of California, Berkeley
arxiv_id: '2610.01235'
url: https://arxiv.org/abs/2610.01235
pdf_url: https://arxiv.org/pdf/2610.01235
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: LLM Agent 外部控制内化训练
tags:
- LLM Agent
- Harness Annealing
- Control Internalization
- SFT
- Curriculum Learning
one_liner: 提出Harness退火训练框架，实现LLM Agent对外部控制逻辑的内化，降低运行时外部依赖
practical_value: '- 做电商/导购Agent训练时，可将外部控制逻辑（如搜索停止判断、流程跳转决策、回答校验规则）拆为显式THINK监督目标，性能远优于直接对全轨迹做SFT

  - 若现有Agent依赖大量外部控制逻辑（如状态跟踪、工作流编排），可采用强到弱的harness课程训练，逐步将控制逻辑内化到模型权重，降低运行时系统复杂度

  - 训练过程中可搭配强harness轨迹重放、控制提示dropout两个trick，避免控制内化过程中出现任务性能大幅下降

  - 无需追求完全移除所有外部控制：小模型退火到仅保留工具层时性能最优，大模型保留部分外部控制的平均性能更高，可根据部署场景选择checkpoint'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent的运行高度依赖外部harness提供状态跟踪、流程编排、答案校验等控制决策，直接基于harness支撑的成功轨迹做SFT，只会让模型始终依赖外部干预，运行时系统复杂度高、部署成本高，无法轻量化落地。
### 方法关键点
1. 定义4层嵌套harness配置：从仅保留工具调用能力的H1，到包含状态、工作流、校验全量控制的H4，逐层增加控制能力
2. 设计分层推理监督机制：将轨迹拆分为OBS（输入观测）、THINK（控制决策监督目标）、ACT（动作监督目标）三部分，显式监督控制逻辑的生成，而非仅将harness控制信息作为输入上下文
3. 采用强到弱的课程训练范式：先基于全量harness轨迹做初始SFT，再逐步引入更弱harness的轨迹训练，搭配强harness轨迹重放、控制提示dropout两个trick，避免性能退化
### 关键实验结果
基于Qwen3.5 9B和35B模型在SWE-QA、SWE-QA-Pro数据集测试：9B模型的H2-targeted checkpoint在仅工具部署（H1）下，比全harness训练的基线分别高5.01、3.09分，跨harness性能波动从5.48降至0.57；分层监督比直接全轨迹SFT在弱harness部署下性能提升超40分，完全避免了弱支撑下的性能崩溃。
### 最值得记住的一句话
模型与harness是协同进化关系，当模型可可靠承担某类控制责任时，对应的运行时外部引导即可移除，harness优化可聚焦于模型仍存在缺陷的环节。
