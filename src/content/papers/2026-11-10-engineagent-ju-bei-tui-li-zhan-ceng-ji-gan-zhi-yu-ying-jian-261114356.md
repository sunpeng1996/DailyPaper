---
title: 'EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack
  Hierarchy Awareness and Hardware Abilities'
title_zh: EngineAgent：具备推理栈层级感知与硬件能力的端侧LLM推理引擎Agent化系统
authors:
- Zhengxiang Huang
- Yujie Sun
- Shengheng Chen
- Zhaode Wang
- Chaoyue Niu
- Zeyu Zhao
- Chengfei Lv
- Fan Wu
- Guihai Chen
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
arxiv_id: '2611.14356'
url: https://arxiv.org/abs/2611.14356
pdf_url: https://arxiv.org/pdf/2611.14356
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 端侧LLM推理引擎自动化适配
tags:
- On-Device-LLM
- Coding-Agent
- Inference-Engine
- Hardware-Acceleration
- Multi-Agent
one_liner: 实现端侧LLM推理引擎新模型适配自动化，端到端成功率较SOTA编码Agent从33.3%提升至75%
practical_value: '- 做复杂分层业务系统（如推荐引擎召回/排序模块、端侧推荐SDK）的Agent自动化迭代时，可复用层级感知知识索引思路：先抽象系统功能层级，将代码实体映射到对应层级并明确跨层依赖，避免修改局部代码时遗漏关联模块的适配

  - 做跨环境（离线训练/在线推理/端侧部署）的Agent自动化部署时，可提前预构建各环境的build/test/debug可复用技能集，用已验证的成熟流程做基准，大幅降低环境适配的试错成本

  - 复杂工程类Agent任务可复用Builder/Debugger/Auditor三角色分工模式：权责拆分+红队独立校验的协作范式，比单Agent完成率更高、错误率更低

  - 预构建的领域知识库可采用增量更新机制，仅修改受代码变更影响的子图，本方案中增量更新成本仅为初始构建的2.5%，适配业务系统频繁迭代的场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
端侧LLM架构迭代极快（部分模型更新间隔仅24天），移动硬件异构性强，新模型适配推理引擎需要跨转换、构图、算子、硬件后端多层协同修改，人工适配成本高、周期长（最长达30天）。现有通用编码Agent不感知推理引擎的层级依赖，无法处理主机-设备跨路径的调试问题，端到端适配成功率仅33.3%。
### 方法关键点
- 预构建**层级感知引擎知识索引**：将推理引擎代码结构映射到9层抽象层级（输入/图/算子三大层拆分），捕获跨层依赖关系，增量更新成本仅为初始构建的0.7%
- 预构建**硬件感知调试技能集**：针对CPU/GPU/NPU不同后端，用已支持模型预验证编译、部署、测试、Debug全流程，形成可复用的单元测试与故障排查样例，增量更新成本仅为初始构建的3.5%
- 多Agent协同主循环：Builder对比新模型与已支持模型的架构差异，基于知识索引做分层修改；Debugger调用预构建技能做故障定位；Auditor做分层校验+端侧端到端验证，迭代直到全链路通过
### 关键实验
在12个适配任务上测试，覆盖3款移动端LLM、4组推理引擎-后端对（MNN/llama.cpp/MLC-LLM/ExecuTorch，CPU/Vulkan/OpenCL/QNN），对比SWE-Agent、OpenCode、Codex等基线：EngineAgent端到端成功率达75%，是最强基线Codex（33.3%）的2.25倍；单任务平均耗时降低13.7%，LLM API成本降低24.2%。
### 核心结论
面向复杂分层异构系统的Agent自动化落地，首先要做领域专属的抽象知识建模，而非直接套用通用编码Agent。
