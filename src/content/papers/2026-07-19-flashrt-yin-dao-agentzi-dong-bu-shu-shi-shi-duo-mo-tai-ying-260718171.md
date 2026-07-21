---
title: 'FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications'
title_zh: FlashRT：引导Agent自动部署实时多模态应用的代理框架
authors:
- Krish Agarwal
- Zhuoming Chen
- Yanyuan Qin
- Zhenyu Gu
- Atri Rudra
- Beidi Chen
affiliations:
- Carnegie Mellon University
- AMD
- University at Buffalo
arxiv_id: '2607.18171'
url: https://arxiv.org/abs/2607.18171
pdf_url: https://arxiv.org/pdf/2607.18171
published: '2026-07-19'
collected: '2026-07-21'
category: Agent
direction: Agent 多模态服务部署优化
tags:
- Coding Agent
- Multimodal Serving
- Deployment Optimization
- Chain-of-Program
- GPU Inference
one_liner: 提出chain-of-program范式引导编码Agent自动优化多模态应用部署，最高实现70×延迟降低、3.6×吞吐量提升
practical_value: '- 复用chain-of-program范式优化Agent工作流：当用Coding Agent处理推荐系统多模态pipeline优化、广告素材生成服务部署等复杂任务时，不要要求Agent一步输出最终方案，先引导其将原始实现转换为带依赖标注的分层IR做静态分析，再生成候选优化方案，可大幅降低Agent出错概率、提升优化效果

  - 多模态推理部署可参考内置的性能tradeoff策略：对低延迟敏感的实时推荐/直播交互场景，优先将关联模块同置降低通信开销；对高吞吐量要求的批量素材生成场景，优先拆分无状态依赖的模块做流水线并行，可快速得到符合业务性能要求的部署方案

  - 多硬件适配场景引入Agent自动优化降本：针对AMD等GPU优化生态不完善的硬件，可基于FlashRT框架自动搜索部署策略，无需硬件专家手工调优就能得到超过vLLM-Omni等主流开源方案的性能（如Qwen3-Omni在AMD
  MI355X上延迟降低65%）'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
实时多模态应用（语音Agent、交互式视频生成、数字人等）需将异构模型组合为复杂pipeline部署，现有服务系统和自动并行编译器受限于固定策略、场景覆盖窄，新应用的高效部署依赖手工定制，人力成本极高无法适配多模态应用快速迭代的需求。

### 方法关键点
- 提出chain-of-program范式：引导Coding Agent先将用户提供的单GPU参考实现转换为分层中间表示（IR），标注节点的持久化状态读写属性、边的阻塞/流式属性，准确捕获数据依赖和状态作用域；再通过顺序解释器验证IR正确性，做静态分析识别所有可行的优化方向
- 设计自驱动验证迭代循环：Agent基于IR分析结果初始化候选优化队列，每轮迭代独立实现候选方案，自行构造模拟真实用户输入的测试用例验证功能正确性、benchmark目标性能，根据实测结果更新候选队列、重排优化优先级，直到所有候选方案都完成验证

### 关键实验
在NVIDIA B200、AMD MI355X两类GPU上测试5类典型多模态应用，对比单GPU基线、vLLM-Omni等专家实现：B200上最高实现70×延迟降低、2.8×吞吐量提升；AMD MI355X上最高实现70×延迟降低、3.6×吞吐量提升，Qwen3-Omni文本转音频场景性能比专家实现vLLM-Omni高65%。

### 核心结论
对复杂的系统优化任务，给Agent提供结构化的工作流引导（分层IR转换+实测反馈循环），比直接要求Agent端到端输出的效果提升数个量级，甚至可超过特定领域的专家手工实现。
