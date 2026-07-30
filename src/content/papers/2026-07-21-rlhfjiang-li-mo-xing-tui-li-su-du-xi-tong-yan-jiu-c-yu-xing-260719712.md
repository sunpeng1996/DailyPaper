---
title: How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference
  Runtimes for RLHF
title_zh: RLHF奖励模型推理速度系统研究：C++与PyTorch运行时对比
authors:
- Venkata Naga Sai Vishnu Rohit Pulipaka
- Anish Katta
- Deva Rohit Reddy Peddireddy
arxiv_id: '2607.19712'
url: https://arxiv.org/abs/2607.19712
pdf_url: https://arxiv.org/pdf/2607.19712
published: '2026-07-21'
collected: '2026-07-30'
category: Training
direction: RLHF训练 · 奖励模型推理性能优化
tags:
- RLHF
- Reward Model
- Inference Optimization
- ONNX Runtime
- torch.compile
- Performance Benchmarking
one_liner: 量化对比RLHF奖励模型多类推理后端性能，给出CPU/GPU场景下的最优部署选型指引
practical_value: '- 业务中使用RLHF做推荐/Agent偏好对齐时，CPU部署无需重写C++代码，直接将奖励模型导出为ONNX格式用Python调用，即可获得1.7x左右的推理加速，性价比极高

  - GPU部署优先选择torch.compile做奖励模型推理，相比C++ ONNX Runtime的p50延迟低30%、p95延迟低78%，仅需承担输入形状变化带来的少量重编译开销

  - 无论CPU/GPU都禁用naive padding的默认batching策略，会导致吞吐量下降5~8倍；GPU场景改用长度感知分桶batching，吞吐量可比单条推理提升35%，CPU场景直接单条推理即可，batching无收益

  - 所有推理性能benchmark必须基于多次独立进程启动的结果计算置信区间，单次运行的结果误差极大，会严重误导部署选型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLHF训练流程中奖励模型打分是策略更新的前置阻塞步骤，当前工业界普遍默认使用PyTorch eager或torch.compile作为推理后端，从未系统量化不同方案的真实性能差异；而打分与策略生成争抢同一份CPU/GPU算力，更快的打分引擎可释放更多资源给生成环节，也能降低整体训练耗时，因此需要明确不同场景下的最优选型。
### 方法关键点
- 自研基于ONNX Runtime的C++推理引擎，原生实现SentencePiece/WordPiece两种分词逻辑，端到端无PyTorch依赖
- 先做正确性验证：与PyTorch参考结果的最大误差CPU为5.7e-6、GPU为4.2e-3，符合浮点误差容忍范围
- 对比基线覆盖PyTorch eager、torch.compile、FastAPI封装的PyTorch服务三类主流方案，测试CPU/GPU两类硬件
- 所有性能结果均为多次独立进程启动的均值+95%置信区间，排除单次运行的系统噪声干扰
### 关键结果
基于Anthropic hh-rlhf数据集采样的60条不同长度样本测试：
- CPU场景：C++ ONNX Runtime引擎p50延迟335.9ms，比PyTorch各基线快1.7~1.9x；且Python调用ONNX Runtime性能与C++版本几乎无差异，加速核心来自图执行而非C++语言本身
- GPU场景：torch.compile的p50延迟19.0ms、p95延迟25.6ms，比C++引擎分别快30%、78%，仅比PyTorch eager/FastAPI快1~1.2x
- naive batching会导致CPU吞吐量下降5~8倍、GPU下降3.5~4倍；仅GPU场景下长度感知分桶batching可将吞吐量提升35%，CPU场景batching无收益
### 核心结论
没有通用最优的推理后端选型，所有性能结论都要结合硬件场景实测，且单次benchmark结果不可信，必须做多次独立启动的统计验证。
