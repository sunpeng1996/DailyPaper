---
title: Test-Time Scaling for Diffusion Language Models with Frequency-Aware Remasking
title_zh: 基于频率感知重掩码的扩散语言模型测试时缩放方法
authors:
- Bowen Zuo
- Yue Yu
- Dongruo Zhou
- Yinglun Zhu
affiliations:
- University of California, Riverside
- Indiana University
arxiv_id: '2611.10486'
url: https://arxiv.org/abs/2611.10486
pdf_url: https://arxiv.org/pdf/2611.10486
published: '2026-11-06'
collected: '2026-11-12'
category: LLM
direction: 扩散语言模型 · 推理优化
tags:
- Diffusion Language Model
- Test-Time Scaling
- Remasking
- Decoding Optimization
- Reasoning
one_liner: 提出两阶段自适应推理策略，用频率感知重掩码解决扩散LM假置信度问题，提升推理性能
practical_value: '- 生成式推荐/电商文案生成场景若使用Diffusion LM，可复用两阶段自适应推理架构：先用低成本base采样器处理大部分简单请求，仅对效果不达标的难请求启用频率感知重掩码，平衡推理效率与生成质量

  - 遇到生成结果多样性不足、反复采样仍收敛到平庸/错误结果的场景，可借鉴频率感知重掩码思路：跟踪token跨去噪步的变化频率，优先提交高频波动token，避免假置信度锁死生成路径，提升难样本的生成效果

  - 做LLM推理/Agent推理优化时，可复用SAFE自适应阈值选择逻辑：无需手动调整频率阈值，自动识别稳定的高波动token组，降低策略落地的调参成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有扩散语言模型（DLM）推理普遍基于瞬时置信度/熵的重掩码策略，存在假置信度缺陷：局部置信度高的token可能属于局部自洽但全局错误的推理路径，导致多次采样仍收敛到相同错误结果，硬推理、代码生成等场景性能瓶颈明显，仅靠增加采样次数的传统测试时缩放方法无法解决该问题。
### 方法关键点
- 两阶段自适应测试时缩放框架：第一阶段用低成本置信度驱动的base采样器处理所有请求，一旦检测到正确解就停止计算，避免算力浪费；第二阶段仅对base阶段未解决的难请求启用频率感知重掩码，算力优先倾斜到难样本
- 频率感知重掩码规则：跟踪每个token的预测结果在去噪步中的变化频率，反转常规提交顺序，优先提交高频变化的token，让不同样本在模型未确定的位置分支探索，避免收敛到单一错误路径
- 自适应SAFE选择策略：自动基于频率分布的最大间隔识别高频率token组，仅当频率信号区分度足够且连续两步稳定时才启用频率规则，否则回退到base策略，保证推理稳定性
### 关键实验
在MATH-500数学推理、HumanEval代码生成数据集上测试，对比Elimination等强自适应基线：LLaDA-8B、Dream-7B分别获得最高3.73%、7.33%的绝对准确率提升，HumanEval上最高获得11.39%、10.98%的绝对覆盖率提升；对base策略采样100次仍无解的难样本，仅用16次频率感知采样就能恢复3.75%~18.75%的正确解。
### 核心结论
扩散LM的假置信度问题无法通过单纯增加采样次数解决，通过轨迹级信号调整token提交顺序、优先开放不确定位置的探索，可以在可控算力开销下大幅提升难样本性能。
