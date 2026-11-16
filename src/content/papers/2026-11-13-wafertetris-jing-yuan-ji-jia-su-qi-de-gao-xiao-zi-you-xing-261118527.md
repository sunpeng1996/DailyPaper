---
title: 'WaferTetris: Efficient Freeform Mapping on Wafer-Scale Accelerators'
title_zh: WaferTetris：晶圆级加速器的高效自由形态映射系统
authors:
- Dayou Du
- Congjie He
- Andrew Boutros
- Luo Mai
- Vaughn Betz
- Jianyi Cheng
affiliations:
- University of Edinburgh
- University of Waterloo
- University of Toronto
arxiv_id: '2611.18527'
url: https://arxiv.org/abs/2611.18527
pdf_url: https://arxiv.org/pdf/2611.18527
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM硬件加速 · 晶圆级引擎映射
tags:
- Wafer-Scale Accelerator
- LLM Inference
- FPGA P&R
- Spatial Mapping
- KV Cache
one_liner: 复用FPGA布局布线算法实现晶圆级加速器无模板自由映射，提升LLM解码吞吐量与上下文长度上限
practical_value: '- 做大模型推理服务选型时，可参考晶圆级加速器的自由映射方案，将KV cache容量、上下文长度上限提升1.8倍，适配长会话电商Agent、长文本商品理解、长序列用户行为建模等场景

  - 自研大模型推理/多任务调度框架的团队，可复用其基于recurrence的全局吞吐量预估模型，解决分支-合并依赖下的瓶颈误判问题，优化集群资源利用率

  - 资源受限场景下的并行任务调度可借鉴其类俄罗斯方块的无固定模板资源打包思路，避免固定配额导致的资源碎片化，提升GPU/ASIC集群的任务吞吐量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
晶圆级加速器（如Cerebras WSE系列）集成数十万计算单元（PE），能为LLM训练、推理提供远超传统GPU集群的算力密度，但现有映射方案依赖固定矩形模板分配PE资源，导致严重的空间碎片化：WSE-3上运行LLaMA3.1-8B解码时约40%的PE和本地内存被闲置，不仅拉低吞吐量，还限制了KV cache可用空间，压缩上下文长度上限，且手动优化模板的适配成本极高，无法快速迭代。

### 方法关键点
- 取消PE岛的固定几何约束，采用类俄罗斯方块的自由形态打包策略，在保留原有PE任务代码、逻辑连接不变的前提下，充分利用碎片化PE资源
- 设计基于recurrence的吞吐量预估模型，全局建模分支-合并路径的累计延迟，比传统单最慢单元瓶颈预估的精度高90%+，可高效指导空间并行度分配
- 构建适配WSE路由规则的FPGA架构抽象，新增per-color门控单元，让成熟的FPGA布局布线（P&R）算法可直接生成符合WSE硬件约束的合法映射
- 引入分块规划策略，将百万级PE的全局映射拆分为子问题，单次映射+编译耗时控制在40分钟以内

### 关键实验结果
在Cerebras WSE-3上测试，对比自动模板映射基线CU.POKer，LLM解码吞吐量最高提升4.42倍，PE利用率从50%左右提升至93%以上；对比手动优化的WaferLLM，LLaMA3.1-8B的最大支持上下文长度从44k提升至80k（+1.8倍），相同上下文下的单用户吞吐量最高提升1.1倍。

### 核心洞见
成熟领域经过充分验证的算法，经过针对性的抽象适配后，往往能跨领域解决全新场景的复杂问题，效果甚至超过定制化手动优化方案
